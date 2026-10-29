"""Resampling is tested as a plain function, without a browser."""

import shutil
import subprocess
from dataclasses import replace
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.server.app import create_app

ROOT = Path(__file__).resolve().parents[1]


def test_resampler_sample_counts_continuity_clipping_and_silence():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the plain JavaScript resampler test")
    script = r"""
      import fs from 'node:fs';
      import assert from 'node:assert/strict';
      const source = fs.readFileSync('web/mic/resampler.js');
      const url = 'data:text/javascript;base64,' + source.toString('base64');
      const {createResampler} = await import(url);
      for (const rate of [44100, 48000]) {
        const convert = createResampler(rate);
        const output = [];
        const input = Float32Array.from({length:rate}, (_, i) => Math.sin(i / 100));
        for (let offset = 0; offset < input.length; offset += 128) {
          output.push(...convert(input.subarray(offset, offset + 128)));
        }
        assert.equal(output.length, 50);
        assert(output.every(frame =>
          frame instanceof Int16Array && frame.length === 320));
        const whole = createResampler(rate)(input);
        assert.deepEqual(output, whole);
      }
      const samples = [[0, 0], [0.5, 16384], [2, 32767], [-2, -32768]];
      for (const [sample, expected] of samples) {
        const frames = createResampler(48000)(new Float32Array(960).fill(sample));
        assert.equal(frames.length, 1);
        assert(frames[0].every(value => value === expected));
      }
    """
    result = subprocess.run(
        [node, "--input-type=module", "-e", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr


def test_mic_route_injects_engine_port_and_serves_worklet():
    config = replace(Config(), STT_MIC_PORT=9876)
    with TestClient(create_app(config=config)) as client:
        page = client.get("/mic")
        assert page.status_code == 200
        assert 'data-engine-port="9876"' in page.text
        assert "__STT_" not in page.text
        assert client.get("/mic/worklet.js").status_code == 200
        assert client.get("/mic/resampler.js").status_code == 200

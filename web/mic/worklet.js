import {createResampler} from './resampler.js';

class MicProcessor extends AudioWorkletProcessor {
  constructor() {
    super();
    this.convert = createResampler(sampleRate);
    this.generation = 0;
    this.port.onmessage = ({data}) => {
      if (data.type === 'reset') {
        this.convert = createResampler(sampleRate);
        this.generation = data.generation;
      }
    };
  }
  process(inputs) {
    const input = inputs[0]?.[0];
    if (input) {
      for (const pcm of this.convert(input)) {
        let energy = 0;
        for (const sample of pcm) energy += (sample / 32768) ** 2;
        this.port.postMessage({pcm: pcm.buffer, level: Math.sqrt(energy / pcm.length),
          generation: this.generation}, [pcm.buffer]);
      }
    }
    return true;
  }
}
registerProcessor('minefield-mic', MicProcessor);

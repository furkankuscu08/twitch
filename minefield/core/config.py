"""Runtime defaults. Environment parsing belongs to entrypoints."""

import math
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class Config:
    GAME_PORT: int = 8100
    PLANT_PORT: int = 8101
    STT_BACKEND: str = "flux"
    DEEPGRAM_REGION: str = "eu"
    CONFIRM_N: int = 2
    MIN_WORD_PROB: float = 0.6
    AGREE_TOL_S: float = 0.5
    FINAL_SOLO_MIN_PROB: float = 0.7
    ARM_DELAY_S: float = 30
    MAX_MINES: int = 4
    HAND_SIZE: int = 6
    CODE_TTL_S: float = 300
    FALSE_ALARM_WINDOW_S: float = 10
    RECEIPT_WORDS: int = 8
    CHAT_MAX_CHARS: int = 500
    ENGINE_TIMEOUT_S: float = 5
    CHAT_SEND_TIMEOUT_S: float = 5
    WS_CLIENT_QUEUE_SIZE: int = 100
    MAX_PENDING_PLANTS: int = 1000
    STT_MIC_PORT: int = 8765
    STT_AUDIO_QUEUE_SIZE: int = 4
    STT_LAG_WINDOW: int = 100
    STT_HEARTBEAT_S: float = 2
    STT_HTTP_TIMEOUT_S: float = 2
    STT_RECONNECT_MIN_S: float = 0.5
    STT_RECONNECT_MAX_S: float = 8

    def __post_init__(self):
        for item in fields(self):
            value = getattr(self, item.name)
            if isinstance(value, str):
                continue
            if isinstance(value, bool) or not math.isfinite(value) or value < 0:
                raise ValueError(f"Invalid {item.name}")
            if item.type is int and (not isinstance(value, int) or value < 1):
                raise ValueError(f"Invalid {item.name}")
        if not 0 <= self.MIN_WORD_PROB <= 1 or not 0 <= self.FINAL_SOLO_MIN_PROB <= 1:
            raise ValueError("Confidence must be between zero and one")
        if max(self.GAME_PORT, self.PLANT_PORT, self.STT_MIC_PORT) > 65535:
            raise ValueError("Invalid port")
        if self.STT_BACKEND not in {"flux", "nova3"}:
            raise ValueError("Invalid backend")
        if self.DEEPGRAM_REGION not in {"eu", "us"}:
            raise ValueError("Invalid region")
        if min(self.ENGINE_TIMEOUT_S, self.CHAT_SEND_TIMEOUT_S) <= 0:
            raise ValueError("Timeouts must be positive")
        if (
            min(self.STT_HEARTBEAT_S, self.STT_HTTP_TIMEOUT_S, self.STT_RECONNECT_MIN_S)
            <= 0
        ):
            raise ValueError("STT intervals must be positive")
        if self.STT_RECONNECT_MAX_S < self.STT_RECONNECT_MIN_S:
            raise ValueError("Invalid STT reconnect bounds")

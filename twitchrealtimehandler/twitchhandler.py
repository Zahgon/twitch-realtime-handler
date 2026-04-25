# -*- coding: utf-8 -*-

"""
Parent classes for twitch-realtime-handler
"""

import queue
import subprocess
from dataclasses import dataclass, field
from threading import Thread
from typing import Union

import numpy as np
import streamlink


@dataclass
class _TwitchHandler:
    twitch_url: Union[str, None] = None
    chunk_size: int = 2**8
    quality: str = "480p"
    _stream_url: Union[str, None] = None

    def get_stream_url(self) -> None:
        """Retrieve the url of the rtmp stream from twitch url using streamlink"""
        pass


@dataclass
class _TwitchHandlerAudio:
    """Default values for audio"""

    rate: int = 16000  # sampling rate in Hz
    segment_length: float = 2  # length of the audio segment
    quality: str = "audio_only"


@dataclass
class _TwitchHandlerVideo:
    """Default values for video"""

    rate: int = 30  # sampling rate in Hz
    quality: str = "480p"


@dataclass
class _TwitchHandlerGrabber(_TwitchHandler):
    """Parent class for the Audio and Image Grabber"""

    queue_size: int = 1000
    blocking: bool = False
    _th_reader: Union[Thread, None] = field(init=False)
    _n_bytes_per_payload: Union[int, None] = field(init=False)
    _cmd_pipe: Union[list, None] = field(init=False)
    _reshape_size: Union[list, None] = field(init=False)
    dtype: type = field(init=False)
    _terminate: bool = False
    _ffmpeg_process: Union[subprocess.Popen, None] = field(init=False)
    _auto_start: bool = True

    def __post_init__(self):
        self._fifo = queue.Queue(maxsize=self.queue_size)
        self._ffmpeg_process = None
        self._th_reader = None

    def terminate(self):
        """Stop the reader thread and terminate the ffmpeg process"""
        pass

    def _reader(self):
        """Launch the ffmpeg process, read its output pipe, and store it into a queue"""
        pass

    def _start_thread(self):
        pass

    def grab(self) -> Union[None, np.ndarray]:
        """Return the image or audio segment"""
        pass

    def grab_raw(self) -> Union[bytes, None]:
        pass

    def _bytes_to_array(self, in_bytes: bytes) -> np.ndarray:
        """
        Args:
            - in_bytes (bytes): audio segment or frame as bytes

        Returns:
        the frame as a np.ndarray (RGB)
        or a segment as a np.ndarray
        """
        pass

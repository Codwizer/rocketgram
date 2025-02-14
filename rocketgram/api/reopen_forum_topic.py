# Copyright (C) 2015-2023 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class ReopenForumTopic(BoolResultMixin, Request):
    """\
    Represents ReopenForumTopic request object:
    https://core.telegram.org/bots/api#reopenforumtopic
    """

    chat_id: Union[int, str]
    message_thread_id: int

# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union, Optional

from .request import Request
from .utils import BoolResultMixin


@dataclass(frozen=True)
class EditForumTopic(BoolResultMixin, Request):
    """\
    Represents EditForumTopic request object:
    https://core.telegram.org/bots/api#editforumtopic
    """

    chat_id: Union[int, str]
    name: int
    icon_color: Optional[int] = None
    icon_custom_emoji_id: Optional[str] = None

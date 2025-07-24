# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing definitions for the result type.

It works like Rust's Result type.
"""

import dataclasses
from typing import Generic, TypeAlias, TypeVar

_T = TypeVar("_T")
_E = TypeVar("_E")


@dataclasses.dataclass(frozen=True)
class Ok(Generic[_T]):
  value: _T


@dataclasses.dataclass(frozen=True)
class Error(Generic[_E]):
  error: _E


Result: TypeAlias = Ok[_T] | Error[_E]

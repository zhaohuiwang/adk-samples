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

"""Module containing definitions for the capabilities in CaMeL."""

import dataclasses
from typing import Any, Self

from . import readers
from . import sources


@dataclasses.dataclass(frozen=True)
class Capabilities:
  """Capabilities for a value."""

  sources_set: frozenset[sources.Source]
  readers_set: readers.Readers[Any]
  other_metadata: dict[str, Any] = dataclasses.field(default_factory=dict)

  def __hash__(self) -> int:
    return (
        hash(self.sources_set)
        ^ hash(self.readers_set)
        ^ hash(tuple(self.other_metadata.items()))
    )

  @classmethod
  def default(cls) -> Self:
    return cls(frozenset({sources.SourceEnum.USER}), readers.Public())

  @classmethod
  def camel(cls) -> Self:
    return cls(frozenset({sources.SourceEnum.CAMEL}), readers.Public())

# Copyright 2017 CodiLime
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from veles.schema.plugin import MethodSignature, BroadcastSignature
from veles.schema import fields


method_hello = MethodSignature(
    'hello',
    fields.String(),
    fields.String(),
)

broadcast_hello = BroadcastSignature(
    'hello',
    fields.String(),
    fields.String(),
)

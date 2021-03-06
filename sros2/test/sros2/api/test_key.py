# Copyright 2019 Open Source Robotics Foundation, Inc.
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

from sros2.api import _key


def test_is_key_name_valid():
    # Valid cases
    assert _key._is_key_name_valid('/foo')
    assert _key._is_key_name_valid('/foo/bar')
    assert _key._is_key_name_valid('/foo/bar123/_/baz_')

    # Invalid cases
    assert not _key._is_key_name_valid('')
    assert not _key._is_key_name_valid(' ')
    assert not _key._is_key_name_valid('//')
    assert not _key._is_key_name_valid('foo')
    assert not _key._is_key_name_valid('foo/bar')
    assert not _key._is_key_name_valid('/42foo')
    assert not _key._is_key_name_valid('/foo/42bar')

# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests import unittest, mock

import boto3


class TestTableResourceCustomizations(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.resource = boto3.resource('dynamodb', 'us-east-1')

    def test_resource_has_batch_writer_added(self):
        table = self.resource.Table('mytable')
        self.assertTrue(hasattr(table, 'batch_writer'))

# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack, LLC
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Functional test case that tests logging output"""

import os
import unittest

from tests import functional
from tests.utils import execute


class TestLogging(functional.FunctionalTest):

    """Functional tests for Glance's logging output"""

    def test_verbose_debug(self):
        """
        Test logging output proper when verbose and debug
        is on.
        """

        self.cleanup()
        api_port, reg_port, conf_file = self.start_servers()

        # The default functional test case has both verbose
        # and debug on. Let's verify that debug statements
        # appear in both the API and registry logs.

        self.assertTrue(os.path.exists(self.api_log_file))

        api_log_out = open(self.api_log_file, 'r').read()

        self.assertTrue('DEBUG [glance-api]' in api_log_out)

        self.assertTrue(os.path.exists(self.registry_log_file))

        registry_log_out = open(self.registry_log_file, 'r').read()

        self.assertTrue('DEBUG [glance-registry]' in registry_log_out)

        self.stop_servers()

    def test_no_verbose_no_debug(self):
        """
        Test logging output proper when verbose and debug
        is off.
        """

        self.cleanup()
        api_port, reg_port, conf_file = self.start_servers(debug=False,
                                                           verbose=False)

        self.assertTrue(os.path.exists(self.api_log_file))

        api_log_out = open(self.api_log_file, 'r').read()

        self.assertFalse('DEBUG [glance-api]' in api_log_out)

        self.assertTrue(os.path.exists(self.registry_log_file))

        registry_log_out = open(self.registry_log_file, 'r').read()

        self.assertFalse('DEBUG [glance-registry]' in registry_log_out)

        self.stop_servers()
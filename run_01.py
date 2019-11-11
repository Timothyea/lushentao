#!/user/bin/env python
# -*- conding:utf-8 -*-
import pytest

pytest.main(["-s","-v","test_case/test_prod.py","--alluredir","report/xml"])
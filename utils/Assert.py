# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 4:34 下午 
# @Author  : cyq
# @File    : Assert.py


from utils.Log import get_log

log = get_log()


class Assert:

    @staticmethod
    def assert_unequal(exp, res):
        try:
            log.info("ASSERT UNEQUAL: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            assert exp != res
            return True
        except AssertionError as e:
            log.error("ASSERT UNEQUAL ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_equal(exp, res):

        try:
            log.info("ASSERT EQUAL: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            assert exp == res
            return True
        except AssertionError as e:
            log.error("ASSERT EQUAL ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_in(exp, res):
        try:
            log.info("ASSERT IN: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            assert exp in res
            return True
        except AssertionError as e:
            log.error("ASSERT IN ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_body(exp: dict, res: dict):

        for k, v in exp.items():
            if k in res:
                try:
                    assert res[k] == exp[k]
                    log.info(f"ASSERT BODY: EXPECT IS [{exp[k]}] RESULT IS [{res[k]}]")
                    return True
                except AssertionError as e:
                    log.error(f"ASSERT BODY: EXPECT IS [{exp[k]}] RESULT IS [{res[k]}]")
                    raise e
            else:
                log.error(f"ASSERT BODY ERROR: RESULT BODY NON-EXISTENT [{k}] \n EXPECT IS [{exp}] RESULT IS [{res}]")
                raise AssertionError

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        """测试单个答案能否会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English",my_survey.responses)#测试是否在列表中
    def test_store_three_responses(self):
        """测试三个答案能否会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English","Spanish","Mandarin"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()#此时完成了两次测试，每次测试都会运行test_store_single_response()和test_store_three_responses()，并报告每个测试都通过了。
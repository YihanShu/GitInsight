class BaseAnalyzer:
    """
    所有分析器的统一接口
    """

    def analyze(self, commit, diff_text):
        raise NotImplementedError
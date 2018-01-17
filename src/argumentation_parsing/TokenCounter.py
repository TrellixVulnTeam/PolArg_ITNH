class TokenCounter:

    def countTokens(self, sentence_to_count):
        # only needed if sentence_to_count is a string
        token_list = ' '.join(self, sentence_to_count)
        token_count = len(token_list)

        return token_count

    def count_Article_Token(self, article_to_count):
        # only needed if article_to_count is a string
        token_list = ' '.join(self, article_to_count)
        token_count = len(token_list)

        return token_count

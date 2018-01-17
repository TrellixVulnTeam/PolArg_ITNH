class TokenCounter:

    def count_tokens(self, sentence_to_count):
        # only needed if sentence_to_count is a string
        token_list = ' '.join(self, sentence_to_count)
        token_count = len(token_list)

        return token_count

    def count_article_token(self, article_to_count):
        # only needed if article_to_count is a string
        token_list = ' '.join(self, article_to_count)
        token_count = len(token_list)

        return token_count

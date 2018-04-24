class TennisJudge:
    SCORE_LIST = ["Love", "Fifteen", "Thirty", "Forty"]
    SAME_SCORE_LIST = ["Love All", "Fifteen All", "Thirty All", "Deuce"]
    ACTION_LIST = ["Adv", "Win"]

    @classmethod
    def judge(cls, player1_name, player2_name, player1_score, player2_score):
        if cls.is_same_score(player1_score, player2_score):
            return cls.show_same_text_score(player1_score)
        elif cls.is_ready_to_win(player1_score, player2_score):
            return cls.show_leader_action(player1_name, player1_score, player2_name, player2_score)
        else:
            return cls.show_text_score(player1_score, player2_score)

    @classmethod
    def show_same_text_score(cls, player1_score):
        return cls.SAME_SCORE_LIST[player1_score]

    @classmethod
    def show_leader_action(cls, player1_name, player1_score, player2_name, player2_score):
        return cls.is_leader(player1_name, player2_name, player1_score, player2_score) + " " + cls.ACTION_LIST[
            abs(player1_score - player2_score) >> 1]

    @classmethod
    def show_text_score(cls, player1_score, player2_score):
        return cls.SCORE_LIST[player1_score] + " " + cls.SCORE_LIST[player2_score]

    @staticmethod
    def is_same_score(player1_score, player2_score):
        return player1_score == player2_score

    @staticmethod
    def is_ready_to_win(player1_score, player2_score):
        return player1_score > 3 or player2_score > 3

    @classmethod
    def is_leader(cls, player1_name, player2_name, player1_score, player2_score):
        if player1_score > player2_score:
            return player1_name
        else:
            return player2_name

class Poet:
    poets_counts = 0

    @staticmethod
    def get_poets():
        json = {"prvinaEtsami": 199, "nzami": 313, "mlkalshEraibhar": 856, "hafz": 518, "sEdi": 1393, "frdvsi": 522,
                "snaii": 1534, "rvdki": 452, "khiam": 272, "jami": 843, "shhriar": 136, "mvlvi": 5265}
        poets = list(json.keys())
        Poet.poets_counts = len(poets)
        return poets

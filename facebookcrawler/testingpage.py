# page id 407556572930758
# app id 1272463692838608
# app secret d98ec43247ce415f95504db213526a17
# graph api explorer acess token EAASFTIpmttABAKxJNTuWMvV9ZB2Fkd7GnQjfBwYDEGjjutwAKyZAzeJ86Fh4V4PTMdSqeSWcuq4IE8YJadW1UUfLqhlaZBKgXeDhs3WqVnyAN5MeJS3sW2ZBZB7RBir564C0W6Q4m7jJZCZCuyQegs9wLauHnb5QiZAxDr1YaNleOuPreaMoeBv3oFaUtLDtdaEZD
# access_token= EAASFTIpmttABAHRhQNQuKw6RyEJLQZAvjIBePI2MrQNtalBGsMdHb10qy7DkJjya0RuA79EZC11JLIU11ZB9q8EsrJKQad6MVH94Bow18E8Up0k2ZCXYQeQ2xBTeHuhiUfHajQF5s28qsdDASXAzmahuEvXnQElgqjZA8I6hdogZDZD & expires=5184000

import facebook

def main():


	# Colocando as chaves
	cfg = {"page_id"      : "407556572930758","access_token" : "EAASFTIpmttABAHRhQNQuKw6RyEJLQZAvjIBePI2MrQNtalBGsMdHb10qy7DkJjya0RuA79EZC11JLIU11ZB9q8EsrJKQad6MVH94Bow18E8Up0k2ZCXYQeQ2xBTeHuhiUfHajQF5s28qsdDASXAzmahuEvXnQElgqjZA8I6hdogZDZD"}
	api = get_api(cfg)
	msg = "Fuck Society testing 2"
	status = api.put_wall_post(msg)
def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])
	resp = graph.get_object('me')
	return graph


if __name__ == "__main__":
	main()
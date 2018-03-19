import collections
import re

token_map = {'+':'PLUS', 
'-':'MINUS', 
'*':'MULT', 
'/':'DIV', 
'(':'LPAR', 
')':'RPAR'}

variables = {'A': 0, 'B': 0, 'C':0}

grammer = ["NUM ADD NUM",
"NUM SUB NUM",
"NUM MUL NUM",
"NUM DIV NUM"]

def main_calc(expr):
	expr_tokenized = Tokenizer(expr)
	print(expr_tokenized.tokens)
	expr_parsed = Parse(expr_tokenized.tokens)
	return expr_parsed.result

class Parse:
	def __init__(self, tokens):
		self.counter = 0
		self.tokens = tokens
		self.token = self.tokens[self.counter]
		self.result = self.expression()

		self.get_next_token()
		if self.token == 'end':
			print('ok')
		else:
			print('not at end')

	def expression(self):
		component1 = self.factor()

		self.get_next_token()

		while self.token[0] in ['PLUS', 'MINUS']:

			if self.token[0] == 'PLUS':
				component2 = self.factor()
				component1 += component2
			else:
				component2 = self.factor()
				component1 -= component2

			self.get_next_token()
		self.revert()

		return component1

	def factor(self):
		factor1 = self.number()

		self.get_next_token()

		while self.token[0] in ['MULT', 'DIV']:
			if self.token[0] == 'MULT':
				factor2 = self.number()
				factor1 = factor1 * factor2
			else:
				factor2 = self.number()
				factor1 = factor1 / factor2

			self.get_next_token()
		self.revert()
		return factor1

	def number(self):
		self.get_next_token()

		if self.token[0] == "LPAR":
			value = self.expression()
			self.get_next_token()
		elif self.token[0] == 'NUM':
			value = self.token[1]
		else:
			print('Not a number')

		return value


	def get_next_token(self):
		self.counter = self.counter + 1
		self.token = self.tokens[self.counter]

	def revert(self):
		self.counter = self.counter - 1
		self.token = self.tokens[self.counter]



	


class Tokenizer:
	def __init__(self, expr):
		self.expr = expr
		self.token_list = self.Token_List()
		self.tokens = self.Token()

	def Token_List(self):
		result = re.findall('[\d.]+|[+\-*/()]|[\w.]+', self.expr)
		return result

	def Token(self):
		result = []
		for x in self.token_list:
			try:
				value = float(x)
				name = 'NUM'
			except ValueError:
				if x in token_map:
					value = x
					name = token_map[x]
				elif x in variables:
					value = variables[x]
					name = 'NUM'
				else:
					value = x
					name = 'var'
			result.append((name, value))
		result.append('end')
		result = ['start'] + result
		return result
			


'''if __name__ == '__main__':
	expr = '(5-3)/7'
	x = main_calc(expr)
	print(x)'''


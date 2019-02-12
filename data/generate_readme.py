import pandas as pd

def generate_one_table(df, fp):

	df = df.sort_values(['date', 'paper_link'], ascending=False).reset_index(drop=True)

	print('| Title | Publication | Paper | Link |', file=fp)
	print('| ----- | ----------- | ----- | ---- |', file=fp)

	length = len(df['date'])
	for i in range(length):
		inst = df.loc[i]

		pub = 'arXiv' if pd.isna(inst['publication']) else inst['publication']
		paper = '[[paper]](%s)' % inst['paper_link']
		if 'arxiv' in inst['paper_link']:
			paper = '[[%s]](%s)' % (inst['paper_link'].split('/')[-1], inst['paper_link'])
		project = '[[project]](%s)' % inst['project_link'] if not pd.isna(inst['project_link']) else ''
		if project and 'github.com' in inst['project_link']:
			parts = inst['project_link'].split('/')
			project = '[[%s]](%s)' % ('/'.join([parts[-2], parts[-1]]), inst['project_link'])

		output_str = '| %s | %s | %s | %s |' % (
			inst['title'],
			pub,
			paper,
			project
		)
		print(output_str, file=fp)


def papers(fp, file_list):
	print('## Papers', file=fp)
	for filename in file_list:
		print(filename)
		df = pd.read_csv(filename)
		print('### %s' % (filename.split('.')[0]), file=fp)
		generate_one_table(df, fp)


if __name__ == '__main__':
	fp = open('../README.md', 'w')

	# title
	print('# Cool Fashion Papers 👔👗🕶️🎩', file=fp)

	## Brief
	talk = '__Cool Fashion Related Papers and Resources (datasets, conference, workshops, ...).__\n\n' \
	       'Papers are ordered in arXiv first version submitting time (if applicable).\n\n' \
		   'Feel free to send a PR or issue.\n\n'
	print(talk, file=fp)

	## Papers
	file_list = ['Synthesis.csv',
				 'Classification.csv',
				 'Recommendation.csv',
				 'Forecast.csv']
	papers(fp, file_list)
	print('\n\n', file=fp)

	## Event
	for line in open('event.md').readlines():
		print(line, file=fp)
	print('\n\n', file=fp)

	## Dataset
	for line in open('dataset.md').readlines():
		print(line, file=fp)
	print('\n\n', file=fp)
	
	## Other resources
	for line in open('others.md').readlines():
		print(line, file=fp)
	print('\n\n', file=fp)


	fp.close()





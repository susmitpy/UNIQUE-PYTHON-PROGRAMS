import myparse, re

soup = myparse.parse("http://mahresult.nic.in/hsc2017/HS-SUBJ.htm")

[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]

txt = soup.getText()

subject_row = re.findall(r'\d{1,3} +\d{1,3} +\w[A-Z]+ +', txt)

subjects = [re.search(r'\w[A-Z]+', i).group() for i in subject_row]

subjects_code = [re.search(r'\d{1,3} [A-Z]', i).group()[:-2] for i in subject_row]

sub_code = {i:j for i, j in zip(subjects, subjects_code)}

for i, j in sub_code.items():
    print(i + " : " + j)

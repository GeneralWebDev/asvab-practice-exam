import re, json
h = open('index.html','r',encoding='utf-8').read()
start = h.find('const questions=[')
end = h.find('];', start) + 1
qs_str = h[start+len('const questions='):end]
qs_str = re.sub(r'\{s:', '{"s":', qs_str)
qs_str = re.sub(r',q:', ',"q":', qs_str)
qs_str = re.sub(r',o:', ',"o":', qs_str)
qs_str = re.sub(r',a:', ',"a":', qs_str)
data = json.loads(qs_str)
with open('exam_content.json','w',encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('Saved', len(data), 'questions to exam_content.json')

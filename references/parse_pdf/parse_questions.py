#To Do
#Parse a txt file of answers for correctAnswerIndex
#Print dictionaries to .json file in same formatting as what we manually type out.

output = list()

with open('bronzeq.txt','r') as f:
    lines = f.readlines()
with open('bronzea.txt','r') as f:
    answer_list = f.readlines()

answer_index = list()
for j in range(len(answer_list)):
    if "a" in answer_list[j]:
        answer_index.append(0)
    if "b" in answer_list[j]:
        answer_index.append(1)
    if "c" in answer_list[j]:
        answer_index.append(2)
    if "d" in answer_list[j]:
        answer_index.append(3)

print "Read in " +str(len(answer_index)) + " Answers."

num_lines = len(lines)
i = 0
j = 0
while i < num_lines:

    if "QUESTION" in lines[i]:
       # print i
        question = list()
        answer1 = list()
        answer2 = list()
        answer3 = list()
        answer4 = list()
        while len(lines[i]) > 2:
            question.append(lines[i])
            i += 1
       # print i
        while "A.  " not in lines[i]:
            i += 1
       # print i
        while "B.  " not in lines[i]:
            if len(lines[i]) > 2:
                answer1.append(lines[i])
            i += 1
       # print i
        while "B.  " not in lines[i]:
            i += 1
       # print i
        while "C.  " not in lines[i]:
            if len(lines[i]) > 2:
                answer2.append(lines[i])
            i += 1
       # print i
        while "C.  " not in lines[i]:
            i += 1
       # print i
        while "D.  " not in lines[i]:
            if len(lines[i]) > 2:
                answer3.append(lines[i])
            i += 1
       # print i
        while "D.  " not in lines[i]:
            i += 1
       # print i
        if i >= num_lines:
            break
       # print i, num_lines
        while "QUESTION" not in lines[i]:
            if len(lines[i]) > 2:
                answer4.append(lines[i])
            i += 1
            if i >= num_lines:
                break
       # print i
        i -= 1

        # now remove all "\n" from strings
        question = "".join(question).strip("QUESTION").strip("\n").strip().split()[1:]
        question =  " ".join(question)
        answer1 = "".join(answer1).strip("\n").strip().split()[1:]
        answer1 = " ".join(answer1)
        answer2 = "".join(answer2).strip("\n").strip().split()[1:]
        answer2 = " ".join(answer2)
        answer3 = "".join(answer3).strip("\n").strip().split()[1:]
        answer3 = " ".join(answer3)
        answer4 = "".join(answer4).strip("\n").strip().split()[1:]
        answer4 = " ".join(answer4)
        dictionary = {"question": question,
                      "answers": [answer1,answer2,answer3,answer4],
                      "correctAnswerIndex": answer_index[j],
                      "correctAnswerText": "Correct!",
                      "questionSource": "The British Soaring Association: Bronze Certificate Confuser"
                      }
        j += 1
        #print dictionary
        output.append(dictionary)

        #raw_input("lkdsjafl: ")
    i += 1

print "Read in " +str(len(output)) + " Questions."

with open('parsed_db.json', 'w') as outfile:
    outfile.write("[\n")
    for i in range(len(output)):
        outfile.write("  {\n")

        outfile.write('    "question": "'+output[i]["question"]+'",\n')
        outfile.write('    "answers": [\n')
        outfile.write('      "'+output[i]["answers"][0]+'",\n')
        outfile.write('      "'+output[i]["answers"][1]+'",\n')
        outfile.write('      "'+output[i]["answers"][2]+'",\n')
        outfile.write('      "'+output[i]["answers"][3]+'"\n')
        outfile.write('    ],\n')
        outfile.write('    "correctAnswerIndex": '+str(output[i]["correctAnswerIndex"])+',\n')
        outfile.write('    "correctAnswerText": "'+output[i]["correctAnswerText"]+'",\n')
        outfile.write('    "questionSource": "'+output[i]["questionSource"]+'"\n')
        outfile.write("  }")
        if i < len(output) - 1:
            outfile.write(",\n")
        else:
            outfile.write("\n")
    outfile.write("]")

        

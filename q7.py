# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
a={'name':'Abhishek','Designation':'CEO of navgurukul','Gender':'Male','age':'29'}
with open('teamdital.json','w') as file:
    json.dump(a,file,indent=4)

import numpy as np
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 88, 76, 85],
    [78, 82, 80, 92],
    [95, 78, 88, 90]
])
subjects=['Math', 'Science', 'English', 'History']
average_scores=np.mean(student_scores,axis=0)
highest_avg=np.argmax(average_scores)
for i,subject in enumerate(subjects):  
  print(f"average score in (subjects):{average_scores[i]:.2f}")
print(f"\n the subjects with highest average score:{subjects[highest_avg]}")

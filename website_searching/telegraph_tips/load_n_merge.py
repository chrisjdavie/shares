#!/usr/bin/env python
'''
Created on 15 Aug 2014

@author: chris
'''
tips_fname = '/home/chris/Work/projects/shares/analysed_files/questor/all_tips.p'
import pickle

def main():
    file_tips = load_questor_tips()
#     
#     for tip in file_tips:
#         print tip
#     
#     file_tips.pop(0)
#     file_tips.pop(0)
    
    from initial_open_n_save import dl_questor_tips
    dl_tips = dl_questor_tips()
    
    newer_tips = []
    
    for i, dl_tip in enumerate(dl_tips):
        if dl_tip['time'] > file_tips[0]['time']:
            newer_tips.append(dl_tip)
        else:
            break
    
    comb_tips = newer_tips + file_tips
#     for tip in comb_tips:
#         print tip
    
#     print 'a'
    from operator import itemgetter
    tips_sort = sorted(comb_tips,key=itemgetter('time'))[::-1]
#     print 'b'
    if i > 0:
        import shutil
        shutil.copy2(tips_fname,tips_fname[:-2]+'_clone.p')
        f = open(tips_fname,'w')
        pickle.dump(tips_sort,f)
        f.close()
        
def load_questor_tips():
    
    
    f = open(tips_fname,'r')
    file_tips = pickle.load(f)
    f.close()
    return file_tips      
         

if __name__ == '__main__':
    main()
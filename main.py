## 사용불가 (2024-02-25)
# import module.myPyside6
## 사용불가 (2024-02-25)
# import module.myTkinter as MT
## 사용가능 (2024-02-26)
# import module.myPyQt5 as MMPQ5
## 사용가능 (2024-02-26)
import module.myPyQ5_html_1 as MPPQ5H

def main():
    ## myPyside6의 main 
    # S : 시작
    # myPyside6.start() #myPyside6의 시작하는 함수 사용 불가
    # E : 끝
    
    ## myTkinter의 main 
    # S : 시작
    # app = MT.myTkinterWindowNoMasterVer() # myTkinter를 시작하는 함수 사용 불가
    # app.loop()
    # E : 끝
    
    ## myPyQt5의 main 
    # S : 시작
    # MMPQ5.main()
    # E : 끝
    
    ## myPyQ5_html_1의 main 
    # S : 시작
    MPPQ5H.main()
    # E : 끝
    
    # print("hello")
    
    
if __name__ == ("__main__"):
    main()
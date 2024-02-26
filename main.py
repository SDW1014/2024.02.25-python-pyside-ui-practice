## 사용불가 (2024-02-25)
# import module.myPyside6
## 사용불가 (2024-02-25)
# import module.myTkinter as MT
import module.myPyQt5 as MMPQ5

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
    MMPQ5.main()
    # E : 끝
    
    print("hello")
    
    
if __name__ == ("__main__"):
    main()
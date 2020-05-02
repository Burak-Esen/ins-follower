from time import strftime, sleep
from selenium import webdriver
from random import randint
from selenium.webdriver.common.keys import Keys
import pandas as pd

def commentAndFollow(webdriver, nProfile:int, hashtag_list: list):
    #
    # BURASI HASHTAG LİSTESİ
    #

    #
    #İLK KULLANIMDAN SONRA ALLTAKİ SATIRI YORUM SATIRI YAPIP SONRAKİ İKİ SATIRI TEKRAR YORUM SATIRI OLMAKTAN ÇIKARMAK GEREKİYOR
    prev_user_list = [] # - if it's the first time you run it, use this line and comment the two below
    # prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
    # prev_user_list = list(prev_user_list['0'])

    new_followed = []
    tag = -1
    followed = 0
    likes = 0
    comments = 0

    for hashtag in hashtag_list:
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
        sleep(randint(4,6))
        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        
        first_thumbnail.click()
        sleep(randint(1,2))    
        try:        
            for x in range(1,nProfile+1):
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                
                if username not in prev_user_list:
                    # If we already follow, do not unfollow
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        
                        new_followed.append(username)
                        followed += 1

                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                        
                        button_like.click()
                        likes += 1
                        sleep(randint(18,25))

                        # Comments and tracker
                        comm_prob = randint(1,10)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        if comm_prob > 7: ##### YORUM ORANI %30 
                            comments += 1
                            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                            comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                            #
                            # BURASI YORUMLARIN BULUNDUĞU ALAN YORUMLARDAN BİRİ RASTGELE SEÇİLİYOR
                            #
                            comm_prob = randint(1,10)
                            if (comm_prob < 7):
                                comment_box.send_keys('Really cool!')
                                sleep(1)
                            elif (comm_prob > 6) and (comm_prob < 9):
                                comment_box.send_keys('Nice work :)')
                                sleep(1)
                            elif comm_prob == 9:
                                comment_box.send_keys('Nice gallery!!')
                                sleep(1)
                            elif comm_prob == 10:
                                comment_box.send_keys('So cool! :)')
                                sleep(1)
                            # Enter to post comment
                            comment_box.send_keys(Keys.ENTER)
                            sleep(randint(22,28))

                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(25,29))
                else:
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(20,26))
        # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except:
            continue

    for n in range(0,len(new_followed)):
        prev_user_list.append(new_followed[n])
        
    updated_user_df = pd.DataFrame(prev_user_list)
    updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
    webdriver.close()
    print('Liked {} photos.'.format(likes))
    print('Commented {} photos.'.format(comments))
    print('Followed {} new people.'.format(followed))
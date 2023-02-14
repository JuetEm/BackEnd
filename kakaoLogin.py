from firebase_admin import auth

def createCustomtoken(uid,displayName,email,photoURL) :
    cUid = "kakao:{}".format(uid)
    
    fUser = ''
    customToken = ''
    # USER 여부
    try:
        fUser = auth.get_user(cUid)
        print('Successfully fetched user data: {0}'.format(fUser.uid))

        auth.update_user(cUid, display_name=displayName, email=email, photo_url=photoURL,
                         )

        customToken = auth.create_custom_token(fUser.uid)
        print("update user customToken : {}".format(customToken))
    except Exception as e:
        print("Fialed to fetched user data " + str(e))

        fUser = auth.create_user(
        uid=cUid, display_name=displayName, email=email, photo_url=photoURL,
        )
        print('Sucessfully created new user: {0}'.format(fUser.uid))

        customToken = auth.create_custom_token(fUser.uid)
        print("create user customToken : {}".format(customToken))
        
    return customToken
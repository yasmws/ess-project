
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCh_HTUYjfsVZl6HefvuDFAFRwVmry38tw",
    'authDomain': "aurore-35e60.firebaseapp.com",
    'projectId': "aurore-35e60",
    'storageBucket': "aurore-35e60.appspot.com",
    'messagingSenderId': "194880387139",
    'appId': "1:194880387139:web:f1502cc327764970607cf6",
    'databaseURL': "https://aurore-35e60-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
import firebase from 'firebase/app';
import "firebase/analytics";
import "firebase/auth";
import "firebase/firestore";

const settings = {timestampsInSnapshots: true};

const firebaseConfig = {
    apiKey: "AIzaSyCo3gQ584cvbo0aPKLaiYjky7RbEeHYeOs",
    authDomain: "cmap-ea258.firebaseapp.com",
    databaseURL: "https://cmap-ea258-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "cmap-ea258",
    storageBucket: "cmap-ea258.appspot.com",
    messagingSenderId: "298657047580",
    appId: "1:298657047580:web:26d2514824423326e1abd9",
    measurementId: "G-QXGVDNYKHV"
  };

firebase.initializeApp(firebaseConfig);
firebase.firestore().settings(settings);

export default firebase;


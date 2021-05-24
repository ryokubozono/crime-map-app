import firebase from 'firebase'

const config = {
  apiKey: "AIzaSyDgjOpcwwsVC9tV7MdAX7HtIVPBvPSFIL4",
  authDomain: "blog-betme.firebaseapp.com",
  projectId: "blog-betme",
  storageBucket: "blog-betme.appspot.com",
  messagingSenderId: "1070379729965",
  appId: "1:1070379729965:web:295e39e1321bed09d4a4a4",
  measurementId: "G-4QP6KYRVQ7"
}

const firebaseApp = firebase.initializeApp(config, 'exercise-vue')
const firestore = firebaseApp.firestore()
firestore.settings({ timestampsInSnapshots: true })

export default firestore
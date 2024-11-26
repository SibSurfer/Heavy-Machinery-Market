// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey:  import.meta.env.VITE_API_KEY, //to be seen on the client side
  authDomain: "hmm-site-e198a.firebaseapp.com",
  projectId: "hmm-site-e198a",
  storageBucket: "hmm-site-e198a.firebasestorage.app",
  messagingSenderId: "297473133250",
  appId: "1:297473133250:web:7325620690aa21d932495b"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth()
export const db = getFirestore()
export const storage = getStorage()
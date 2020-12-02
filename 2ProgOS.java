package com.company;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;
public class Main
{

    public static void main(String[] args) throws NoSuchAlgorithmException
    {
        System.out.println("Первый поток");
        MyThread myThread = new MyThread();
        Thread thread = new Thread(myThread);
        thread.start();
        Scanner in=new Scanner(System.in);
        char ar[]= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        String word1="";
        String word2="";
        String word3="3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b";
        System.out.println("хэш\t" +word3);

        boolean stop = true;
        for(int i=0;i< ar.length; i++) {
            for(int j=0; j<ar.length;j++) {
                for(int k=0; k<ar.length;k++) {
                    for(int l=0; l<ar.length;l++) {
                        for(int m=0; m<ar.length;m++) {
                            char[] br = {ar[i],ar[j],ar[k],ar[l],ar[m]};
                            word1= String.valueOf(br);
                            word2=sha256(word1);
                            if(generate(word2, word3)) {
                                word2.equals(sha256(word1));
                                System.out.print("исходник:"+word1+"\t");
                                if (word2.equals(word3))break;

                            }
                        }
                    }
                }
            }

        }
        System.out.print(word1 + " " + word2);
    }
    private static boolean generate(String Word2, String Word3)
    {
        if(Word2.equals(Word3))
            return true;
        else
            return false;

    }
    public static String sha256(String word) throws NoSuchAlgorithmException{
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[]hashInBytes = md.digest(word.getBytes(StandardCharsets.UTF_8));

        StringBuilder sb = new StringBuilder();
        for (byte e : hashInBytes) {
            sb.append(String.format("%02x", e));
        }
        String word2 = sb.toString();
        return word2;
    }
}

class MyThread implements Runnable{

    public void run() {
        System.out.println("Второй поток");
        Scanner in=new Scanner(System.in);
        char ar[]= {'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k','j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b','a'};
        String word1="";
        String word2="";
        String word3="1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad";
        System.out.println(" хэш\t" + word3);

        boolean stop = true;
        for(int i=0;i< ar.length; i++) {
            for(int j=0; j<ar.length;j++) {
                for(int k=0; k<ar.length;k++) {
                    for(int l=0; l<ar.length;l++) {
                        for(int m=0; m<ar.length;m++) {
                            char[] br = {ar[i],ar[j],ar[k],ar[l],ar[m]};
                            word1= String.valueOf(br);
                            try {
                                word2=sha256_1(word1);
                            } catch (NoSuchAlgorithmException e) {
                                e.printStackTrace();
                            }
                            if(generate(word2, word3)) {
                                try {
                                    word2.equals(sha256_1(word1));
                                } catch (NoSuchAlgorithmException e) {
                                    e.printStackTrace();
                                }
                                //System.out.print("исходник:"+word1);
                                if (word2.equals(word3))break;

                            }
                        }
                    }
                }
            }

        }
        System.out.print(word1 + " " + word2);
    }
    private static boolean generate(String Word2, String Word3)
    {
        if(Word2.equals(Word3))
            return true;
        else
            return false;

    }
    public static String sha256_1(String word) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[]hashInBytes = md.digest(word.getBytes(StandardCharsets.UTF_8));

        StringBuilder sb = new StringBuilder();
        for (byte e : hashInBytes) {
            sb.append(String.format("%02x", e));
        }
        String word2 = sb.toString();
        return word2;
    }
}
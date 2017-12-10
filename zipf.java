/* -----------------------------------------------------------------------------------
#
#   File:       zipf.java
#   Author:     David Weber
#   Date:       Nov 27, 2017
#   Version:    1.0
#
#	Project:	Spotify Puzzle -- Zipf's Song
#
#
#   Contents:   This program first obtains the total # of songs, n, as well as the 
#				# of best songs we want to be displayed, m. It then gets user input
#				in the form of an integer f (# of times the song was listened to) and
#				a string s (title of the song). Zepf's Law then calculates the quality
#				for each entry i and added to a new array. From there it is just a 
#				mission of displaying the songs of max quality in descending order.
#
#	Algorithm:	Zepf's Law: 
#					quality_i = f_i / z_i,      where z_i = 1 / (i+1) 
#
#												[assuming our arrays start at 0]
#
 ----------------------------------------------------------------------------------- */
import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
 
public class zipf {
 
	 public static void main(String[] args)
	 {
	 	
		/*-------------- initialization ---------------*/
		
		System.out.println("Please enter n, number of songs, and m, the number of songs to select (sep. by space):");
		
		Scanner line = new Scanner(System.in);
		int n = line.nextInt();
		int m = line.nextInt();
		
		//Arrays
		int[] arr1;
		String[] arr2;
		double[] quality;
		String[] max;
		arr1 = new int[n];
		arr2 = new String[n];
		quality = new double[n];
		max = new String[m];
		
		
		
		/*--------------- gets input, calculates quality ----------------*/
		
		System.out.println("Enter: (num) (song_name)");
		for(int i = 0; i < n; i++)
		{
		
			int k = line.nextInt();
			String s = line.next();
			
			//line.nextLine();
			arr1[i] = k;
			arr2[i] = s;
			
			// Zepf's Law
			// q_i = f_i / z_i 
			//	   = f_i / (1 / i)
			double denom = 1.0 / (i + 1.0);
			quality[i] = k / denom;
			
		}
		line.close();
		
		
		/*-------- finds maxval in quality, saves string --------*/
		
		for(int i = 0; i < m; i++)
		{
			// Finds current largest element, saves index.
			double largestElem = 0;
			int index = 0;
			for(int j = 0; j < n; j++)
			{
				if(quality[j] > largestElem)
				{
					largestElem = quality[j];
					index = j;
				}
			}
			
			// Final songs to be output
			max[i] = arr2[index];
			
			// sets highest value to 0 to protect against repeating
			quality[index] = 0;
		
		}
		
		
		/*----------- displays bests songs -----------*/
		
		for(int i = 0; i < m; i++)
		{
			System.out.println(max[i]);
		}
		
	}
	
	
	
	
}

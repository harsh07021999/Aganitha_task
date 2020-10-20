
=================
Spoken To Written
=================
This is a Python module which can that can convert a paragraph of spoken english to written english.

 For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

+++++++++++++
Installation:
+++++++++++++

  Please ensure that you have **updated pip3** to the latest version before installing spoken2written

  You can install the module using Python Package Index using the below command.

.. code-block:: python

   >>python3 setup.py install  



+++++
Usage:
+++++


	Sample Input:-
 Enter Your paragraph in english:
        Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 A M. I always come home after 7 P M. I earn hundred dollars per day. My contact number contains double 5, quadruple
8, single 9 and triple 4.

The input English Paragraph:
 " Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 A M. I always come home after 7 P M. I earn hundred dollars per day. My contact number contains double 5, quadruple 8, single 9 and triple 4."

Converted English Paragraph:
 " Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 AM. I always come home after 7 PM. I earn $100 per day. My contact number contains 55, 8888, 9 and 444."

+++++
Note: 
+++++
	**For the Above input paragraph the incorrect output as a result of improper use of spaces after '.' and ','.  			So currently you have to keep in mind while writing the paragraph to consider proper use of spaces. Because this is not 	an intelligence-based program this is simple rule-based. I will keep being updating the rules so that it can cover 		maximum cases.**



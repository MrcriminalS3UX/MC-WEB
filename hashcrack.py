�
���c           @   sn  e  Z e r# d  d  Z � � Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l m	 Z	 d d l
 Z
 d d l m Z d d l m Z e
 j j j e � d Z e j d � d Z d	 Z i d
 d 6Z e GHd �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z  d �  Z! d �  Z" d �  Z# e$ d k rje# �  n  d S(   i    i����N(   t   unquote(   t   RequestException(   t   InsecureRequestWarnings�   [1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : [1;96mNabil-Rahman |[1;0m [V 1.2.2]

[1;32m------------------------------------------
[93m AUTHOR  : Team DarkWeb T-D
[93m GITHUB  : github.com/Nabil-Official
[93m FB      : nabil.404
[1;32m------------------------------------------
t   cleari   i   uE   Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Geckou
   User-Agentc   
   
   C   s�  d } d } x�t  r�y!t j �  } | j | d t d t d t �} t t j	 d | j
 � � } t t i | d 6� } i
 | d d 6| d	 d	 6| d
 d
 6| d d 6|  d 6d d 6d d 6d d 6d d 6| d d 6} | j | d | d | d t d t �} t j	 d | j
 � d } d j t j d d | � � GHPPWq t k
 rh| d 7} | t k r�d GHPq�q t t f k
 r�}	 d j |	 � GHPq Xq Wd  S(   Nu   https://cmd5.com/i    t   headerst   timeoutt   verifyu   id="(.+?)" value="(.*?)"u   Refereru   __EVENTTARGETu   __EVENTARGUMENTu   __VIEWSTATEu   __VIEWSTATEGENERATORu&   ctl00$ContentPlaceHolder1$TextBoxInputu   md5u'   ctl00$ContentPlaceHolder1$InputHashTypeu   查询u!   ctl00$ContentPlaceHolder1$Button1u    u,   ctl00$ContentPlaceHolder1$HiddenFieldAliCodeu&   ctl00$ContentPlaceHolder1$HiddenField1u&   ctl00_ContentPlaceHolder1_HiddenField2u&   ctl00$ContentPlaceHolder1$HiddenField2t   datau4   <span id="LabelAnswer" class="LabelAnswer".*?>(.+?)<u#   [1;31m[*][1;32m DATA-BASE-1 : {0}u   。.*i   u%   [1;31m[-] DATA-BASE-1 : RequestErroru#   [1;31m[-] DATA-BASE-1 : Error: {0}(   t   Truet   requestst   Sessiont   gett   common_headersR   t   Falset   dictt   ret   findallt   textt   postt   formatt   subR   t	   retry_cntt   KeyErrort
   IndexError(
   t   passwdt   urlt   try_cntt   st   reqt   __R   R   t   resultt   e(    (    s   hashcrack.pyt   cmd5/   s:    	!'
c   
   
   C   sn  d } d } x[t  riy� t j �  } | j d j | � d t d t d t �} t j	 d | j
 d � } | r
t j | d j d	 � � d
 } i | d 6|  d 6} | j d j | � d | d t d t d t �} | j �  d j �  } | rd j | d � GHq
d GHn  PWq t k
 r>| d 7} | t k rfd GHPqfq t t f k
 re}	 d j |	 � GHPq Xq Wd  S(   Nu   https://api.pmd5.com/pmd5api/i    u   {0}checkcodeR   R   R   u   koa.sess.pmd5api=([\w=]+)u
   Set-Cookiet   base64u   capchau	   checkcodeu   pwdu   {0}pmd5t   paramsu   resultu#   [1;31m[+] [1;32mDATA-BASE-2 : {0}u!   [1;31m[-] DATA-BASE-2 : NotFoundi   u   [1;31[-] pmd5: RequestErroru   [-] DATA-BASE-2 : Error: {0}(   R   R	   R
   R   R   R   R   R   R   R   R   t   jsont   loadst   decodet   valuesR   R   R   R   (
   R   R   R   R   R   t   pmd5apit   capchaR"   R   R   (    (    s   hashcrack.pyt   pmd5Q   s2    	* '	
c         C   s�  d } d } x�t  r�yKt j �  } i d d 6d d 6d d 6} | j d	 j | � d
 t d | d t d t �} t j	 d | j
 � d } i |  d 6d d 6d d 6| d 6} t t i | d 6� } | j d j | � d | d
 | d t d t d t �} | j d }	 |	 d k rd GHnG |	 d  d k r<d j |	 d � GHn" |	 j d  � d k rYd! GHn d" GHPWq t k
 r�| d# 7} | t k r�d$ GHPq�q t k
 r�}
 d% j |
 � GHPq Xq Wd  S(&   Nu   https://xmd5.com/i    u   jevoyf46098@chacuo.netu   UserNameu   eEZT1FaD&$S*!t3!Y2d0u   Passwordu   登录u   loginsu   {0}user/CheckLog.aspR   R   R   R   u%   checkcode2 type=hidden value="(.+?)">u   hashu
   MD5 解密u   xmd5u   onu   openu
   checkcode2u   Refereru   {0}md5/search.aspR"   t   allow_redirectsu   Locationu   getpass.asp?type=nou   [-] xmd5: NotFoundi   u   getpass.asp?infou   [+] xmd5: {0}i   u   403.aspu   [-] xmd5: checkcode error!u   [+] xmd5: Pay to get plain.i   u   [-] xmd5: RequestErroru   [-] xmd5: Error: {0}(   R   R	   R
   R   R   R   R   R   R   R   R   R   R   R   t   findR   R   R   (   R   R   R   R   R   R   t	   checkcodeR"   R   t   locationR   (    (    s   hashcrack.pyt   xmd5o   s>    	
'	"'
c      
   C   s�  d } d } xrt  r�yt j �  } | j | d t d t d t �} t j d | j	 � d } t
 t i | d 6� } i | d 6|  d	 6} | j d
 j | � d | d | d t d t �} | j	 } t j d | � d }	 t j d | � d }
 |	 j d � d k rd j |	 |
 � GHn d j |	 |
 � GHPWq t k
 r[| d 7} | t k r}d GHPq}q t k
 r|} d j | � GHPq Xq Wd  S(   Nu   https://md5.navisec.it/i    R   R   R   u   name="_token" value="(.+?)">u   Refereru   _tokenu   hashu	   {0}searchR   u   <code>(.*?)</code>u   积分剩余：[-]?\d+u   未能解密u   [-] navisec: {0}{1}u   [+] navisec: {0} {1}i   u   [-] navisec: RequestErroru   [-] navisec: Error: {0}(   R   R	   R
   R   R   R   R   R   R   R   R   R   R   R+   R   R   R   (   R   R   R   R   R   t   _tokenR   R   t   rspR   t   numR   (    (    s   hashcrack.pyt   navisec�   s2    	!0	
c      
   C   s   d } d } x� t  r� y� i |  d 6} t j | d t d | d t d t �} | j } | j d � d k rr d	 GHn1 t j	 d
 | t j
 � d } d j t | � � GHPWq t k
 r� | d 7} | t k r� d GHPq� q t k
 r� } d j | � GHPq Xq Wd  S(   Nu%   https://hashtoolkit.com/reverse-hash/i    u   hashR   R"   R   R   u   No hashes found foru   [-] hashtoolkit: NotFounds%   <a href="/generate-hash/\?text=(.*?)"u#   [1;31m[+] [1;32mDATA-BASE-3 : {0}i   u   [-] hashtoolkit: RequestErroru   [1;31m[-] DATA-BASE-3 : {0}(   R   R	   R   R   R   R   R   R+   R   R   t   SR   R    R   R   R   (   R   R   R   R"   R   R0   t   plainR   (    (    s   hashcrack.pyt   hashtoolkit�   s(    	'	
c         C   s�   d } d } x� t  r� yQ t j d j | |  � d t d t �} | j } | r_ d j | � GHn d GHPWq t k
 r� | d 7} | t k r� d	 GHPq� q Xq Wd  S(
   Nu   http://www.nitrxgen.net/md5db/i    u
   {0}{1}.txtR   R   u#   [1;31m[+][1;32m DATA-BASE-4 : {0}u!   [1;31m[-] DATA-BASE-4 : NotFoundi   u%   [1;31m[-] DATA-BASE-4 : RequestError(	   R   R	   R   R   R   R   R   R   R   (   R   R   R   R   R0   (    (    s   hashcrack.pyt   nitrxgen�   s    	'	
c         C   s�   d } d } x� t  r� yh i |  d 6} t j | d t d | d t �} t j d | j � } | rv d j | d � GHn d	 GHPWq t	 k
 r� | d
 7} | t
 k r� d GHPq� q Xq Wd  S(   NuJ   http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.phpi    u   md5R   R   R   s"   Hashed string</span>:\s(.+?)</div>u#   [1;31m[+][1;32m DATA-BASE-5 : {0}u!   [1;31m[-] DATA-BASE-5 : NotFoundi   u%   [1;31m[-] DATA-BASE-5 : RequestError(   R   R	   R   R   R   R   R   R   R   R   R   (   R   R   R   R   R   R   (    (    s   hashcrack.pyt   myaddr�   s     	!
c      
   C   s�   d } d } x� t  r� y� i |  d 6} t j | d t d | d t d t �} | j } | j d � d k r� t j	 d	 | � d } d
 j
 | � GHn d GHPWq t k
 r� | d 7} | t k r� d GHPq� q t k
 r� } d j
 | � GHPq Xq Wd  S(   Nu   https://md5.gromweb.com/i    u   md5R   R"   R   R   u   succesfully reversedu*   <em class="long-content string">(.*?)</em>u#   [1;31m[+][1;32m DATA-BASE-6 : {0}u!   [1;31m[-] DATA-BASE-6 : NotFoundi   u%   [1;31m[-] DATA-BASE-6 : RequestErroru#   [1;31m[-] DATA-BASE-6 : Error: {0}(   R   R	   R   R   R   R   R   R+   R   R   R   R   R   R   (   R   R   R   R"   R   R0   R4   R   (    (    s   hashcrack.pyt   gromweb�   s(    	'	
c         C   s�   d } d } x� t  r� y~ i |  d 6} t t i d d 6� } t j | d | d | d t �} t j d	 | j � } | r� d
 j	 | d � GHn d GHPWq t
 k
 r� | d 7} | t k r� d GHPq� q t k
 r� } d j	 | � GHPq Xq Wd  S(   Nu/   http://md5.tellyou.top/MD5Service.asmx/HelloMd5i    u
   Ciphertextu   192.168.1.1u   X-Forwarded-ForR"   R   R   u2   <string xmlns="http://tempuri.org/">(.*?)</string>u#   [1;31m[+] [1;32mDATA-BASE-7 : {0}u!   [1;31m[-] DATA-BASE-7 : NotFoundi   u    [1;31m[-] tellyou: RequestErroru#   [[1;31m-] DATA-BASE-7 : Error: {0}(   R   R   R   R	   R   R   R   R   R   R   R   R   R   (   R   R   R   R"   R   R   R   R   (    (    s   hashcrack.pyt   tellyou  s(    	!
c   	   
   C   s=  d } d } x*t  r8y� t j �  } i d d 6d d 6} i d d 6d	 d
 6} | j | d t d | d | d t �i d d 6d d 6|  d 6} | j | d t d | d t �} | j �  } d | k r� d j | d � GHn d GHPWq t	 k
 r| d 7} | t
 k r5d GHPq5q t k
 r4} d j | � GHPq Xq Wd  S(   Nu   http://www.ttmd5.com/do.phpi    u   Useru   cu   doLoginu   mu   uplnwkdc@mail.bccto.meu   hidUseru    c927dc915426c2c89de3330c397fadf9u   hidPasswordR   R"   R   R   u   Decodeu   getMD5u   md5u   plainu#   [1;31m[+][1;32m DATA-BASE-8 : {0}u!   [1;31m[-] DATA-BASE-8 : NotFoundi   u%   [1;31m[-] DATA-BASE-8 : RequestErroru#   [1;31m[-] DATA-BASE-8 : Error: {0}(   R   R	   R
   R   R   R   R   R#   R   R   R   R   (	   R   R   R   R   R"   R   R   R0   R   (    (    s   hashcrack.pyt   ttmd5-  s.    	%!
c      
   C   s�   d } d } x� t  r� yx i |  d 6} t j | d t d | d t d t �} | j �  } d | k ry d	 j | d � GHn d
 j | d � GHPWq t k
 r� | d 7} | t	 k r� d GHPq� q t
 k
 r� } d j | � GHPq Xq Wd  S(   Nu/   https://www.mysql-password.com/api/get-passwordi    u   hashR   R   R   R   u   erroru   [-] mysql_password: {0}u   [+] mysql_password: {0}u   passwordi   u    [-] mysql_password: RequestErroru   [-] mysql_password: Error: {0}(   R   R	   R   R   R   R   R#   R   R   R   R   (   R   R   R   R   R   R   R   (    (    s   hashcrack.pyt   mysql_passwordJ  s&    	'
c         C   s(  t  j d t d |  f � t  j d t d |  f � t  j d t d |  f � g } t |  � d k r� t j d |  � r� | j t  j d t	 d |  d d f � � | j t  j d t
 d |  f � � n.t |  � d k rut j d |  � ru| j t  j d t d |  f � � | j t  j d t	 d |  d	 f � � | j t  j d t	 d |  d f � � | j t  j d t
 d |  f � � nyt |  � d
 k rFt j d |  � rF| j t  j d t d |  f � � | j t  j d t d |  f � � | j t  j d t d |  f � � | j t  j d t d |  f � � | j t  j d t d |  f � � n� t |  � d k r�t j d |  � r�| j t  j d t d |  f � � | j t  j d t d |  f � � n= |  j d � d k r�| j t  j d t	 d |  d f � � n  x | D] } | j �  q�Wx | D] } | j �  qWd  S(   Nt   targett   argsi)   s   \*[0-9a-f]{40}|\*[0-9A-F]{40}i   u   300i(   s   [0-9a-f]{40}|[0-9A-F]{40}u   100i    s   [0-9a-f]{32}|[0-9A-F]{32}i   s   [0-9a-f]{16}|[0-9A-F]{16}t   :i    u   10(   t	   threadingt   ThreadR    R5   R:   t   lenR   t   matcht   appendt   chamd5R;   R2   R)   R6   R7   R8   R9   R+   t   startt   join(   R   t   threadst   t(    (    s   hashcrack.pyt   cracka  s2    0$)%$"%%%$""""%$"%(c          C   s�   d }  x� |  d k r� |  d }  y� t  d � j �  } Hd | GHd GHt j d � Hd GH| r� t d j t j j t j j	 t
 � � d � d	 � � } | j | t j � Wd  QXt | � n  d GHWn t t t f k
 r� Pn XHd
 GHq	 Wd  S(   Ni   u   Hash: [1;35ms$   [1;31m>>[1;32m YOUR HASH : [1;33ms#   [1;31m>>[1;32m START CRACKING....i   s%   [1;34m------------------------------s   {0}\hash.logi    s   a+s,   [1;31m<<< [1;33mTHANKS FOR USING [31m>>> (   t	   raw_inputt   stript   timet   sleept   openR   t   ost   patht   splitt   realpatht   __file__t   writet   linesepRI   t   KeyboardInterruptt
   ValueErrort   EOFError(   t   xR   t   f(    (    s   hashcrack.pyt   main�  s(    
	7	t   __main__(%   R   t   foot   barRL   R#   RO   R   R?   t   urllibR    R	   t   requests.exceptionsR   t$   requests.packages.urllib3.exceptionsR   t   packagest   urllib3t   disable_warningst   logot   systemR   R   R   R    R)   R.   R2   R5   R6   R7   R8   R9   R:   R;   RI   R[   t   __name__(    (    (    s   hashcrack.pyt   <module>   sD   
	"		%									&	
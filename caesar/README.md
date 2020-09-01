## Caesar cipher with unknown rotation

Trying all possible rotations:

```bash
for i in {1..26}; do printf "$i\t"; echo "jyvzzpunaolybipjvunfzpthre" | caesar $i; done
```

Result:

```bash
1	kzwaaqvobpmzcjqkwvogaquisf
2	laxbbrwpcqnadkrlxwphbrvjtg
3	mbyccsxqdrobelsmyxqicswkuh
4	nczddtyrespcfmtnzyrjdtxlvi
5	odaeeuzsftqdgnuoazskeuymwj
6	pebffvatgurehovpbatlfvznxk
7	qfcggwbuhvsfipwqcbumgwaoyl
8	rgdhhxcviwtgjqxrdcvnhxbpzm
9	sheiiydwjxuhkrysedwoiycqan
10	tifjjzexkyvilsztfexpjzdrbo
11	ujgkkafylzwjmtaugfyqkaescp
12	vkhllbgzmaxknubvhgzrlbftdq
13	wlimmchanbylovcwihasmcguer
14	xmjnndiboczmpwdxjibtndhvfs
15	ynkooejcpdanqxeykjcuoeiwgt
16	zolppfkdqeboryfzlkdvpfjxhu
17	apmqqglerfcpszgamlewqgkyiv
18	bqnrrhmfsgdqtahbnmfxrhlzjw
19	crossingtherubicongysimakx
20	dspttjohuifsvcjdpohztjnbly
21	etquukpivjgtwdkeqpiaukocmz
22	furvvlqjwkhuxelfrqjbvlpdna
23	gvswwmrkxlivyfmgsrkcwmqeob
24	hwtxxnslymjwzgnhtsldxnrfpc
25	ixuyyotmznkxahoiutmeyosgqd
26	jyvzzpunaolybipjvunfzpthre
```

## Flag: using rot19
picoCTF{crossingtherubicongysimakx}

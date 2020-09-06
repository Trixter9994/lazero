command ="lua shell-args.lua ".."http://www.baidu.com/link?url=nS2MGJqjJ4zBBpC8yDF8xDh8vibi1lVeE7gGr9UONBu http://www.baidu.com/link?url=mQRln1LKWUncYQMSCUu01Uq09GtFVObdNqylQdFpk3ebBca2mr5AzXeNyG31ljYB3dW5Ke9vJ2nPVEZ08vicwxSK0mVBg5KQWHUMXdqZcs3".." http://www.baidu.com/link?url=WC6cs2jD3KDdYKkp6fqW-hL0TR6n27MYJLf5N1ue2T55tzR8uIF1ujfEz0KeaTAXW5mIufwgfQahRp6Og3EWKK http://www.baidu.com/link?url=HDHXBxioX55wod3Knq0FvCn7EnlKuVnOgTsElGLTH5SloR-UNIM_v4ikZxaqGMV8oT-s28y4I2lCAQDpwJcpRfrxWsZV6jblY6_r9IpiiJ3 http://www.baidu.com/link?url=fJKL_Eo5hdGojfBzE-Nd_e-IUuyGKhLNIlu6QbRHA4TA_gzG3Gn4cXQUCT4AfYiE_eq8zDPHa6pPLpmzXi3Uk_ http://www.baidu.com/link?url=x92AVuOFH-OYeN8mTqn-F3tjkDHdi5OP1D7n0eirOCZPn7l9ZvCeEIUv7v1p5UUScuCxsCBI3UwRrV4c4UXSia http://www.baidu.com/link?url=fJKL_Eo5hdGojfBzE-Nd_e-IUuyGKhLNIlu6QbRHA4TA_gzG3Gn4cXQUCT4AfYiE_eq8zDPHa6pPLpmzXi3Uk_ http://www.baidu.com/link?url=92nL-4ZW7UkxmgFl5n9M9MxvUjnqqFCWa-zh5HYYF9A9kIc-vJG9yvVNuz-ZPb0f http://www.baidu.com/link?url=VJsiIGgwjHxJlGxr95H_igWXK4-LrJsLkegFSsBs6vrF5HiZidO4DyBo5CCsXcd-DTtcezeQUnXGv0QDjQVA-K http://www.baidu.com/link?url=MZjIn3dePQfU4d_8T_Wt6e8N74vwtgdr_HbjBa7ltt-_xA-e68yPuVIk3x4iHR_K-xdYhAiZM6GoYkd5Or6xPq http://www.baidu.com/link?url=hf1TZuGR0XM80cYf5JR0alxK7qjkoNfiH0JUzA54R35IrJK-E0X2Dq9ReF7eybOhqvvzqcmPGr6-EHCF7I2Bb_ http://www.baidu.com/link?url=Hfx-FhfdpjzGHgKNLj0cwNUklbA4YxnB4saeepCciOVTW5X7TyLB-_4943hmqseqpt-qde_a3THwpTj4if4-l_ http://www.baidu.com/link?url=Th4jgRw6D5uvWgNQunM1t1xSvF8K-Pl0mjKl89IlGedkOqt4rmtFf71fnWh3QbRm http://www.baidu.com/link?url=nxtmWDgtcscw2BoAP-mG8jvnIauNroAZQmXwxwssHuiDV6e0EzxDfXsgG4_JOl0- http://www.baidu.com/link?url=J8zAN0uY-bKlasgSCR4-d1MwHbbjfcSDEEcCW6zvxINKYBS60pxTKEF_htmQv1ld"
handle = io.popen(command)
-- do we really have to read outcome from this thread?
-- will it be empty?
result = handle:read("*a")
handle:close()
--result=result..'\d'
--wtf is going on?
-- use local instead of using some functions.
-- print (result)
io.write(result)
-- do not use the fucking print()
-- use io.write() instead.
-- this will add another return causing a trailing empty line
-- appear as a whole while the other return asychronizedly.

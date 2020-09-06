#include <stdio.h>
#include <stddef.h>
#include <iostream>
#include <Windows.h>
#include <conio.h>
#include <Winuser.h>
// the position matters.
// do not mess with the sequence.
// holy shit.
// so what the fuck is delphi?
int kmain();
int main() {
	while(true) {
		Sleep(500);
		kmain();
	}
}
int kmain() {
	CURSORINFO ci;
	ci.cbSize = sizeof(ci);
	// first is to initialize. fucking prick.
//    PCURSORINFO pci = &ci;
//    BOOL k;
// not to assign to external shits.
// fucking protection.
// but I can fucking transfer.
// so what's fucking next?
	if(GetCursorInfo(&ci)) {
		printf("cursor acquired.\n");
	} else {
		printf("failed to acquire cursor.\n");
	}
//    printf("%d\n",k);
// that's real nuts.
// no fucking return shit?
// how to fucking verify?
	printf("%d\n",ci.hCursor);
	ICONINFO ico;
//    if(Get)
// so what's fucking next?
	if(GetIconInfo(ci.hCursor,&ico)) {
		printf("icon acquired.\n");
	} else {
		printf("failed to acquire icon.\n");
	}
	printf("%d %d %d %d %d\n",ico.fIcon,ico.hbmColor,ico.hbmMask,ico.xHotspot,ico.yHotspot);
}
//int fmain() {
////    HCURSOR sample=GetCursor();
//// not to hide the cursor. when using tablet or without physical mouse.
//
////ci.cbSize = sizeof(ci);
//// it is to put things into that struct.
//// what is that 87???
//	while(true) {
//    CURSORINFO ci;
////		PCURSORINFO ci = (PCURSORINFO)malloc(sizeof(CURSORINFO));
//    ICONINFO iconinfo;
////		PICONINFO iconinfo = (PICONINFO)malloc(sizeof(ICONINFO));
//		Sleep(500);
//		int x=GetCursorInfo(ci);
//		// invalid parameter here.
//		// how the fuck can you get it right?
//		// what the heck please?
//		if(x!=0) {
//			printf("cursor info success\n");
//		}  else {
//			printf("cursor failed: %d\n",GetLastError());
//			continue;
//		}
//		printf("%d %d\n", ci.hCursor,sizeof(ci));
//		int y=GetIconInfo(ci.hCursor,iconinfo);
//		if(y!=0) {
//			printf("icon info success\n");
//		}  else {
//			printf("icon failed: %d\n",GetLastError());
//			continue;
//		}
//		printf("%d\n", iconinfo.fIcon);
//		// what does nonzero mean?      -> true.
////    printf(" %d \n",true);
////    if (iconinfo.fIcon)      {
////    }
////    printf("%d\n",);
//		// is it true or false?
////		free(iconinfo);
////		free(ci);
//		// how the fuck can we get the data?
//		// does that work?
//		// even have typo correction!
//		// what is that fucking Beep?
//	}
////if (!GetCursorInfo(&ci)) {
////    cout << "GetCursorInfo() failed" << endl;
////    return 1;
////}
////cout << ci.hCursor << endl; // ci.hCursor is 0x00000000
//}


#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
#include <windows.h>
#include <tlhelp32.h>

static std::string globalFlag = "647632724a422d06395b08021450166a57783d5b6c68510104723a45526e6b77134e4b1718";

bool debuggerCheck() {
    // Check IsDebuggerPresent
    if (IsDebuggerPresent()) {
        return true;
    }

    // Check Known Debugging Tools
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot != INVALID_HANDLE_VALUE) {
        PROCESSENTRY32 pe;
        pe.dwSize = sizeof(PROCESSENTRY32);
        if (Process32First(hSnapshot, &pe)) {
            do {
                if (strcmp(pe.szExeFile, "ida64.exe") == 0 ||
                    strcmp(pe.szExeFile, "ollydbg.exe") == 0 ||
                    strcmp(pe.szExeFile, "x64dbg.exe") == 0) {
                    CloseHandle(hSnapshot);
                    return true;
                }
            } while (Process32Next(hSnapshot, &pe));
        }
        CloseHandle(hSnapshot);
    }

    // Check PEB debugger flags
    HMODULE hNtDll = GetModuleHandle(TEXT("ntdll.dll"));
    if (hNtDll) {
        // Obtain the address of the NtQueryInformationProcess function directly
        auto NtQueryInformationProcess = (LONG (NTAPI *)(HANDLE, ULONG, PVOID, ULONG, PULONG))
            GetProcAddress(hNtDll, "NtQueryInformationProcess");

        if (NtQueryInformationProcess) {
            ULONG ulSize = 0;
            void* pbi = nullptr;
            // Query for the PEB address
            LONG status = NtQueryInformationProcess(GetCurrentProcess(), 0, pbi, 0, &ulSize);

            if (status == 0) { // STATUS_SUCCESS
                // Allocate buffer and query again
                pbi = malloc(ulSize);
                if (pbi) {
                    status = NtQueryInformationProcess(GetCurrentProcess(), 0, pbi, ulSize, &ulSize);
                    if (status == 0) { // STATUS_SUCCESS
                        // Access PEB and check BeingDebugged flag (offset 2)
                        BYTE* peb = (BYTE*)((ULONG_PTR)pbi + 0x18); // PEB address from the PBI structure
                        if (*(peb + 0x02)) {
                            free(pbi);
                            return true;
                        }
                    }
                    free(pbi);
                }
            }
        }
    }

    return false;
}

void noFlagHere() {
    std::vector<int> fKey = {0x36,0x65,0x36,0x66,0x37,0x34,0x35,0x66,0x34,0x31,0x36,0x65,0x35,0x66,0x35,0x38,0x33,0x30,0x35,0x32,0x35,0x66,0x36,0x62,0x36,0x35,0x37,0x39,0x32,0x31};
    
    std::string asciiF;
    asciiF.reserve(globalFlag.size() / 2);

    for (size_t i = 0; i < globalFlag.length(); i += 2) {
        std::string byteF = globalFlag.substr(i, 2);
        asciiF += static_cast<char>(std::stoi(byteF, nullptr, 16));
    }
    
    for (size_t i = 0; i < asciiF.length(); ++i) {
        asciiF[i] ^= fKey[(i+5)%fKey.size()];
    }
}

void favoriteBug() {
    std::string favoriteBug;

    std::cout << "What is your favorite bug? > ";
    std::getline(std::cin, favoriteBug);

    std::cout << "Wow " << favoriteBug << " is my favorite bug too!" << std::endl;
}

int main() {
    if (debuggerCheck()) {
        std::cout << "Debugger detected!" << std::endl;
        Sleep(1500);
        return 1;
    } else {
        noFlagHere();
        favoriteBug();
        Sleep(1500);
    }
    return 0;
}

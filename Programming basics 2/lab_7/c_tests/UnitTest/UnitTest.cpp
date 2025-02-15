#include "pch.h"
#include "CppUnitTest.h"
#include "../Project/main.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest
{
	TEST_CLASS(UnitTest)
	{
	public:
		
		TEST_METHOD(try_expon)
		{
			Assert::AreEqual(expon(2, 3), 8);
			Assert::AreEqual(expon(3, 2), 9);
			Assert::AreEqual(expon(-2, 3), -8);
			Assert::AreEqual(expon(0, 0), 1);
			Assert::AreEqual(expon(2, 0), 1);
		}
	};
}

# email = "sansarchhetri@mail.yahoo.com"
# username, domain_part = email.split("@")
# domain1, tld1 = domain_part.rsplit(".", 1)
# domain2, extra, tld2 = domain_part.split(".")
# print(domain1, tld1)
# print(domain2, extra, tld2)
# if not domain1:
#     print("domain missing")
# if not domain2:
#     print("domain 2 missing!!")


# print("\n" + "=" * 100)
# print(f"{'ID':<10} {'Name':<25} {'Email':<35} {'Created On':<15}")
# print("=" * 100)

# print(f"{'ID':<10} {'Name':<25} {'Email':<35} {'Created On':<15}")


a, b, c = [int(x) for x in input("enter a  vlaue: ").split()]


if a + b > c and b + c > a and a + c > b:
    print("done!")

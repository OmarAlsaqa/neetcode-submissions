class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "None#,#,"
        if type(strs[0]) == type("str"):
            return "#,".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None#,#,":
            return []
        if type(s) == type("str"):
            return s.split("#,")
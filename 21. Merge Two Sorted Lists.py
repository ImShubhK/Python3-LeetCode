class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = dummyList = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyList.next = list1
                list1 = list1.next
            else:
                dummyList.next = list2
                list2 = list2.next
            dummyList = dummyList.next
        
        if list1:
            dummyList.next = list1
        if list2:
            dummyList.next = list2
        return newList.next
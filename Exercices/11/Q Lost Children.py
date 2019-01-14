# -------------------------------------------
#   Solution par Wiaux Bastien ( @wiauxb )
# -------------------------------------------
child = first_child
while child.next_child() != first_child:
    if not child.is_next_valid():
        return False
    child = child.next_child()
return True

# -------------------------------------------
#   Solution par ( @rverschuren ) 
# -------------------------------------------
current = first_child

while current.is_next_valid():
    current = current.next_child()
    if current is first_child:
        return True
return False

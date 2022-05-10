<template>
  <div class="flex flex-col w-full m-auto">
    <div class="mt-20">
      <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div
            class="
              container
              mx-auto
              flex flex-wrap
              p-5
              flex-col
              md:flex-row
              items-center
              "
          >
            <table class="shadow-md
              overflow-hidden 
              sm:px-6 
              lg:px-8 
              sm:rounded-lg 
              min-w-full 
              divide-y 
              divide-gray-200
              ">
              <thead class="bg-gray-50">
                <tr>
                  <th
                    scope="col"
                    class="
                      px-2
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Name
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Message
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Email
                  </th>
                  <th scope="col" class="relative px-6 py-3">
                    <span class="sr-only">Edit</span>
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
                <tr v-for="message in messages" :key="message.id" @click="toMessageView(message[1].id); isSeen(message[1].id)" :class="message[1].was_seen ? 'bg-gray-100' : 'bg-white'" class="cursor-pointer hover:bg-gray-50">
                  <div v-if="!message[1].was_seen">
                    <td class="px-3 py-4 whitespace-nowrap">
                      <div class="flex items-left">
                        <div>
                          <div class="w-3 h-3 rounded-full bg-blue-400"></div>
                        </div>
                      </div>
                    </td>
                  </div>
                  <div v-else>
                    <td class="px-3 py-4 whitespace-nowrap">
                      <div class="flex items-left">
                        <div>
                        </div>
                      </div>
                    </td>
                  </div>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left">
                      <div>
                        <div class="text-sm font-medium text-gray-900">
                          {{ message[1].name }}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left text-sm text-gray-900">
                        <div class="overflow-hidden truncate w-32 text-left">
                            {{ message[1].message}}
                        </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left"> 
                      <span
                        class="
                          px-2
                          inline-flex
                          text-xs
                          leading-5
                          font-semibold
                          rounded-full
                          bg-yellow-200
                          text-yellow-600
                        "
                      >
                      </span>
                    </div>
                  </td>
                  
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <div class="flex items-left"> 
                      {{ message[1].email }}
                    </div> 
                  </td>
                 
                  <td
                    class="
                      px-6
                      py-4
                      whitespace-nowrap
                      text-right text-sm
                      font-medium
                    "
                  >
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref} from "vue";
export default {
  name: "ContactInboxModule",
  props: ["messages"],
  setup() {
    
    const seenStatus = ref(false);

    async function isSeen(message_id){
       await fetch(`${process.env.SERVER_URL}/admin/seen_message/${message_id}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
      }).then((res) => {
        if (res.status === 200) {
          seenStatus.value = !seenStatus.value;
        } else {
          alert("Failed to mark message");
        }
      });
    }
  
  function toMessageView(message_id) { 
      window.location.href = `/admin/view/message?id=${message_id}`; 

    };
    return {
      seenStatus,
      isSeen,
      toMessageView,
    };
  },
};
</script>

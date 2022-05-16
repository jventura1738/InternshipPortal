<template>
  <div id="listing-form" class="listing-form">
    <div class="p-5 mb-24">
      <div class="mx-4 p-4">
        <div class="flex items-center">
          <div class="flex items-center text-white relative">
            <div
              class="rounded-full transition duration-500 ease-in-out h-12 w-12 py-3 border-2 border-red-600 bg-red-600"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-bookmark"
              >
                <path
                  d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"
                ></path>
              </svg>
            </div>
            <div
              class="absolute top-0 -ml-10 text-center mt-16 w-32 text-xs font-medium uppercase text-red-600"
            >
              General
            </div>
          </div>
          <div
            class="w-1/4 flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="generalToSpecifications"
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="rounded-full transition duration-500 ease-in-out h-12 w-12 py-3 border-2"
              :class="generalToSpecifications"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-list"
              >
                <line x1="8" y1="6" x2="21" y2="6"></line>
                <line x1="8" y1="12" x2="21" y2="12"></line>
                <line x1="8" y1="18" x2="21" y2="18"></line>
                <line x1="3" y1="6" x2="3.01" y2="6"></line>
                <line x1="3" y1="12" x2="3.01" y2="12"></line>
                <line x1="3" y1="18" x2="3.01" y2="18"></line>
              </svg>
            </div>
            <div
              class="absolute top-0 -ml-10 text-center mt-16 w-32 text-xs font-medium uppercase"
              :class="specificationsText"
            >
              Specifications
            </div>
          </div>
          <div
            class="w-1/4 flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="specificationsToReview"
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="rounded-full transition duration-500 ease-in-out h-12 w-12 py-3 border-2"
              :class="specificationsToReview"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-globe"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path
                  d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                ></path>
              </svg>
            </div>
            <div
              class="absolute top-0 -ml-10 text-center mt-16 w-32 text-xs font-medium uppercase"
              :class="reviewText"
            >
              Review
            </div>
          </div>
          <div
            class="w-1/4 flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="reviewToConfirm"
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="rounded-full transition duration-500 ease-in-out h-12 w-12 py-3 border-2"
              :class="reviewToConfirm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-database"
              >
                <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
              </svg>
            </div>
            <div
              class="absolute top-0 -ml-10 text-center mt-16 w-32 text-xs font-medium uppercase"
              :class="confirmText"
            >
              Confirm
            </div>
          </div>
        </div>
      </div>
    </div>
    <General
      :nameChangedCallback="updateName"
      :addressChangedCallback="updateAddress"
      :cityChangedCallback="updateCity"
      :stateChangedCallback="updateState"
      :zipChangedCallback="updateZip"
      :class="{ hidden: isGeneralHidden, '': !isGeneralHidden }"
    />
    <Specifications
      :titleChangedCallback="updatePositionTitle"
      :minQualChangedCallback="updateMinQualifications"
      :prefQualChangedCallback="updatePrefQualifications"
      :posResChangedCallback="updatePositionResponsibilities"
      :addInfoChangedCallback="updateAdditionalInfo"
      :durationChangedCallback="updateDuration"
      :appOpenChangedCallback="updateAppOpen"
      :appCloseChangedCallback="updateAppClose"
      :appLinkChangedCallback="updateApplicationLink"
      :class="{ hidden: isSpecificationsHidden, '': !isSpecificationsHidden }"
    />
    <Review
      :name="clientName"
      :address="clientAddress"
      :city="clientCity"
      :state="clientState"
      :zip="clientZip"
      :positionTitle="positionTitle"
      :minQual="minQualifications"
      :prefQual="prefQualifications"
      :posResp="positionResponsibilities"
      :addInfo="additionalInfo"
      :duration="duration"
      :app_open="app_open"
      :app_close="app_close"
      :app_link="applicationLink"
      :class="{ hidden: isReviewHidden, '': !isReviewHidden }"
    />
    <Confirm
      :submitListingCallback="submitListing"
      :class="{ hidden: isConfirmHidden, '': !isConfirmHidden }"
    />
    <Modal
      v-if="show_modal"
      :ModalTitleProp="modal_title"
      :ModalCloseCallback="closeModal"
      :ModalMessageProp="modal_message"
    />
    <div class="flex justify-center align-center mt-4 mb-4">
      <div
        class="flex justify-center align-center mt-4 mb-4"
        v-if="stepIndex > 0"
      >
        <button class="text-center" @click="previousSection">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-arrow-left"
          >
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
      </div>
      <div
        class="flex justify-center align-center mt-4 mb-4"
        v-if="stepIndex < 3"
      >
        <button class="text-center" @click="nextSection">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-arrow-right"
          >
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import General from "./steps/General.vue";
import Specifications from "./steps/Specifications.vue";
import Review from "./steps/Review.vue";
import Confirm from "./steps/Confirm.vue";
import Modal from "../components/Modal.vue";
export default {
  name: "ListingForm",
  components: {
    General,
    Specifications,
    Review,
    Confirm,
    Modal,
  },
  setup() {
    const isGeneralHidden = ref(false);
    const isSpecificationsHidden = ref(true);
    const isReviewHidden = ref(true);
    const isConfirmHidden = ref(true);
    const stepIndex = ref(0);
    const generalToSpecifications = ref("border-gray-300");
    const specificationsText = ref("text-gray-500");
    const specificationsToReview = ref("border-gray-300");
    const reviewText = ref("text-gray-500");
    const reviewToConfirm = ref("border-gray-300");
    const confirmText = ref("text-gray-500");
    const clientName = ref("");
    const clientAddress = ref("");
    const clientCity = ref("");
    const clientState = ref("");
    const clientZip = ref("");
    const positionTitle = ref("");
    const minQualifications = ref("");
    const prefQualifications = ref("");
    const positionResponsibilities = ref("");
    const additionalInfo = ref("");
    const duration = ref("");
    const app_open = ref("");
    const app_close = ref("");
    const applicationLink = ref("");
    const show_modal = ref(false);
    const modal_title = ref("");
    const modal_message = ref("");

    function closeModal() {
      show_modal.value = false;
    }

    function nextSection() {
      if (
        isGeneralHidden.value == false &&
        isSpecificationsHidden.value == true
      ) {
        if (
          clientName.value != "" &&
          clientAddress.value != "" &&
          clientCity.value != "" &&
          clientState.value != "" &&
          clientZip.value != ""
        ) {
          isGeneralHidden.value = true;
          isSpecificationsHidden.value = false;
          stepIndex.value = 1;
          generalToSpecifications.value =
            "border-red-600 bg-red-600 text-white";
          specificationsText.value = "text-red-600";
        } else {
          show_modal.value = true;
          modal_title.value = "Missing Information";
          modal_message.value =
            "Please fill out all required fields before proceeding.";
        }
      } else if (
        isSpecificationsHidden.value == false &&
        isReviewHidden.value == true
      ) {
        if (
          positionTitle.value != "" &&
          minQualifications.value != "" &&
          prefQualifications.value != "" &&
          positionResponsibilities.value != "" &&
          duration.value != "" &&
          app_open.value != "" &&
          app_close.value != ""
        ) {
          isSpecificationsHidden.value = true;
          isReviewHidden.value = false;
          stepIndex.value = 2;
          specificationsToReview.value = "border-red-600 bg-red-600 text-white";
          reviewText.value = "text-red-600";
        } else {
          show_modal.value = true;
          modal_title.value = "Missing Information";
          modal_message.value =
            "Please fill out all required fields before proceeding.";
        }
      } else if (
        isReviewHidden.value == false &&
        isConfirmHidden.value == true
      ) {
        isReviewHidden.value = true;
        isConfirmHidden.value = false;
        stepIndex.value = 3;
        reviewToConfirm.value = "border-red-600 bg-red-600 text-white";
        confirmText.value = "text-red-600";
      }
      window.scrollTo(0, 0);
    }

    function previousSection() {
      if (
        isGeneralHidden.value == true &&
        isSpecificationsHidden.value == false
      ) {
        isGeneralHidden.value = false;
        isSpecificationsHidden.value = true;
        stepIndex.value = 0;
        generalToSpecifications.value = "border-gray-300";
        specificationsText.value = "text-gray-500";
      } else if (
        isSpecificationsHidden.value == true &&
        isReviewHidden.value == false
      ) {
        isSpecificationsHidden.value = false;
        isReviewHidden.value = true;
        stepIndex.value = 1;
        specificationsToReview.value = "border-gray-300";
        reviewText.value = "text-gray-500";
      } else if (
        isReviewHidden.value == true &&
        isConfirmHidden.value == false
      ) {
        isReviewHidden.value = false;
        isConfirmHidden.value = true;
        stepIndex.value = 2;
        reviewToConfirm.value = "border-gray-300";
        confirmText.value = "text-gray-500";
      }
      window.scrollTo(0, 0);
    }
    function updateName(newName) {
      clientName.value = newName;
    }
    function updateAddress(newAddress) {
      clientAddress.value = newAddress;
    }
    function updateCity(newCity) {
      clientCity.value = newCity;
    }
    function updateState(newState) {
      clientState.value = newState;
    }
    function updateZip(newZip) {
      clientZip.value = newZip;
    }
    function updatePositionTitle(newTitle) {
      positionTitle.value = newTitle;
    }
    function updateMinQualifications(newMinQual) {
      minQualifications.value = newMinQual;
    }
    function updatePrefQualifications(newPrefQual) {
      prefQualifications.value = newPrefQual;
    }
    function updatePositionResponsibilities(newPosResp) {
      positionResponsibilities.value = newPosResp;
    }
    function updateAdditionalInfo(newAddInfo) {
      additionalInfo.value = newAddInfo;
    }
    function updateDuration(newDuration) {
      duration.value = newDuration;
    }
    function updateAppOpen(newAppOpen) {
      app_open.value = newAppOpen;
    }
    function updateAppClose(newAppClose) {
      app_close.value = newAppClose;
    }
    function updateApplicationLink(newLink) {
      applicationLink.value = newLink;
    }
    async function submitListing() {
      console.log("HERERE");
      const body = {
        client_name: clientName.value,
        client_address: clientAddress.value,
        client_city: clientCity.value,
        client_state: clientState.value,
        client_zip: clientZip.value,
        position_title: positionTitle.value,
        pos_responsibility: positionResponsibilities.value,
        min_qualifications: minQualifications.value,
        pref_qualifications: prefQualifications.value,
        additional_info: additionalInfo.value,
        duration: duration.value,
        app_open: app_open.value,
        app_close: app_close.value,
        app_link: applicationLink.value,
      };
      await fetch(`${process.env.SERVER_URL}/listing-submit`, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }).then((res) => {
        console.log(res);
        if (res.status === 200) {
          modal_title.value = "Success!";
          modal_message.value =
            "Your listing has been submitted. An administrator will review it shortly.";
          show_modal.value = true;
          setTimeout(() => {
            window.location.href = "/";
          }, 5000);
        } else {
          modal_title.value = "Failed!";
          modal_message.value =
            "The listing entry has failed. Please try again.";
          show_modal.value = true;
        }
      });
    }
    return {
      isGeneralHidden,
      isSpecificationsHidden,
      isReviewHidden,
      isConfirmHidden,
      stepIndex,
      generalToSpecifications,
      specificationsText,
      specificationsToReview,
      reviewText,
      reviewToConfirm,
      confirmText,
      clientName,
      clientAddress,
      clientCity,
      clientState,
      clientZip,
      positionTitle,
      minQualifications,
      prefQualifications,
      positionResponsibilities,
      additionalInfo,
      duration,
      app_open,
      app_close,
      applicationLink,
      show_modal,
      modal_title,
      modal_message,
      nextSection,
      previousSection,
      updateName,
      updateAddress,
      updateCity,
      updateState,
      updateZip,
      updatePositionTitle,
      updateMinQualifications,
      updatePrefQualifications,
      updatePositionResponsibilities,
      updateAdditionalInfo,
      updateDuration,
      updateAppOpen,
      updateAppClose,
      updateApplicationLink,
      submitListing,
      closeModal,
    };
  },
};
</script>

<style>
#listing-form {
  scroll-behavior: smooth;
  margin: auto;
}
</style>

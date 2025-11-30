---
title: "Metadata"
source: "https://docs.dify.ai/en/use-dify/knowledge/metadata"
author:
  - "[[Authorize Data Source]]"
published:
created: 2025-11-30
description:
tags:
  - "clippings"
---
### Overview

Metadata is information that describes your data - essentially “data about data”. Just as a book has a table of contents to help you understand its structure, metadata provides context about your data’s content, origin, purpose, etc., making it easier for you to find and manage information in your knowledge base.This guide aims to help you understand metadata and effectively manage your knowledge base.

### Core Concepts

- **Field:** The label of a metadata field (e.g., “author”, “language”).
- **Value:** The information stored in a metadata field (e.g., “Jack”, “English”).
![field_name_and_value](https://assets-docs.dify.ai/2025/03/b6a197aa21ab92db93869fcbfa156b62.png)

field\_name\_and\_value

- **Value Count:** The number of values contained in a metadata field，including duplicates. (e.g., “3”).
- **Value Type:** The type of value a field can contain.
	- Dify supports three value types:
		- String: For text-based information
		- Number: For numerical data
		- Time: For dates/timestamps
![value_type](https://assets-docs.dify.ai/2025/03/f6adc7418869334805361535c8cd6874.png)

value\_type

You can create, modify, and delete metadata fields in the knowledge base.

> Any changes you make to metadata fields here affect your knowledge base globally.

**Access the Metadata Panel** To access the Metadata Panel, go to **Knowledge Base** page and click **Metadata**.![metadata_entrance](https://assets-docs.dify.ai/2025/03/bd43305d49cc1511683b4a098c8f6e5a.png)

metadata\_entrance

![metadata_panel](https://assets-docs.dify.ai/2025/03/6000c85b5d2e29a2a5af5e0a047a7a59.png)

metadata\_panel

**Built-in vs Custom Metadata**

|  | Built-in Metadata | Custom Metadata |
| --- | --- | --- |
| Location | Lower section of the Metadata panel | Upper section of the Metadata panel |
| Activation | Disabled by default; requires manual activation | Add as needed |
| Generation | System automatically extracts and generates field values | User-defined and manually added |
| Editing | Fields and values cannot be modified once generated | Fields and values can be edited or deleted |
| Scope | Applies to all existing and new documents when enabled | Stored in metadata list; requires manual assignment to documents |
| Fields | System-defined fields include: - document\_name (string) - uploader (string) - upload\_date (time) - last\_update\_date (time) - source (string) | No default fields; all fields must be manually created |
| Value Types | - String: For text values - Number: For numerical values - Time: For dates and timestamps | - String: For text values - Number: For numerical values - Time: For dates and timestamps |

To create a new metadata field:
1. Click **+Add Metadata** to open the **New Metadata** dialog.
![new_metadata](https://assets-docs.dify.ai/2025/03/5086db42c40be64e54926b645c38c9a0.png)

new\_metadata

1. Choose the value type.
2. Name the field.

> Naming rules: Use lowercase letters, numbers, and underscores only.

![value_type](https://assets-docs.dify.ai/2025/03/f6adc7418869334805361535c8cd6874.png)

value\_type

1. Click **Save** to apply changes.
![save_field](https://assets-docs.dify.ai/2025/03/f44114cc58d4ba11ba60adb2d04c9b4c.png)

save\_field

To edit a metadata field:
1. Click the edit icon next to a field to open the **Rename** dialog.
![rename_field](https://assets-docs.dify.ai/2025/03/94327185cbe366bf99221abf2f5ef55a.png)

rename\_field

1. Enter the new name in the **Name** field.

> Note: You can only modify the field name, not the value type.

![rename_field_2](https://assets-docs.dify.ai/2025/03/2f814f725df9aeb1a0048e51d736d969.png)

rename\_field\_2

1. Click **Save** to apply changes.

> Note: Field changes update across all related documents in your knowledge base.

![same_renamed_field](https://assets-docs.dify.ai/2025/03/022e42c170b40c35622b9b156c8cc159.png)

same\_renamed\_field

To delete a metadata field, click the delete icon next to a field to delete it.

> Note: Deleting a field deletes it and all its values from all documents in your knowledge base.

![delete_field](https://assets-docs.dify.ai/2025/03/022e42c170b40c35622b9b156c8cc159.png)

delete\_field

You can edit metadata in bulk in the knowledge base.**Access the Metadata Editor** To access the Metadata Editor:
1. In the knowledge base, select documents using the checkboxes on the left.
![edit_metadata_entrance](https://assets-docs.dify.ai/2025/03/18b0c435604db6173acba41662474446.png)

edit\_metadata\_entrance

1. Click **Metadata** in the bottom action bar to open the Metadata Editor.
![edit_metadata](https://assets-docs.dify.ai/2025/03/719f3c31498f23747fed7d7349fd64ba.png)

edit\_metadata

**Bulk Add Metadata** To add metadata in bulk:
1. Click **+Add Metadata** in the editor to:
![add_metadata](https://assets-docs.dify.ai/2025/03/d4e4f87447c3e445d5b7507df1126c7b.png)

add\_metadata

- Add existing fields from the dropdown or from the search box.
![existing_field](https://assets-docs.dify.ai/2025/03/ea9aab2c4071bf2ec75409b05725ac1f.png)

existing\_field

- Create new fields via **+New Metadata**.
	> New fields are automatically added to the knowledge base.
![new_metadata_field](https://assets-docs.dify.ai/2025/03/e32211f56421f61b788943ba40c6959e.png)

new\_metadata\_field

- Access the Metadata Panel to manage metadata fields via **Manage**.
![manage_field](https://assets-docs.dify.ai/2025/03/82561edeb747b100c5295483c6238ffa.png)

manage\_field

1. *(Optional)* Enter values for new fields.
![value_for_field](https://assets-docs.dify.ai/2025/03/aabfe789f607a1db9062beb493213376.png)

value\_for\_field

> The date picker is for time-type fields.

![date_picker](https://assets-docs.dify.ai/2025/03/65df828e605ebfb4947fccce189520a3.png)

date\_picker

1. Click **Save** to apply changes.
**Bulk Update Metadata** To update metadata in bulk:
1. In the editor:
- **Add Values:** Type directly in the field boxes.
- **Reset Values:** Click the blue dot that appears on hover.
![reset_values](https://assets-docs.dify.ai/2025/03/01c0cde5a6eafa48e1c6e5438fc2fa6b.png)

reset\_values

- **Delete Values:** Clear the field or delete the **Multiple Value** card.
![multiple_values](https://assets-docs.dify.ai/2025/03/5c4323095644d2658881b783246914f1.png)

multiple\_values

- **Delete fields:** Click the delete icon (fields appear struck through and grayed out).
	> Note: This only deletes the field from this document, not from your knowledge base.
![delete_fields](https://assets-docs.dify.ai/2025/03/1b0318b898f951e307e3dc8cdc2f48d3.png)

delete\_fields

1. Click **Save** to apply changes.
**Set Update Scope** Use **Apply to All Documents** to control changes:
- **Unchecked (Default)**: Updates only documents that already have the field.
- **Checked**: Adds or updates fields across all selected documents.
![apply_all_changes](https://assets-docs.dify.ai/2025/03/4550c68960802c24271492b63a39ad05.png)

apply\_all\_changes

You can edit a single document’s metadata on its details page.**Access Metadata Edit Mode** To edit a single document’s metadata:On the document details page, click **Start labeling** to begin editing.![details_page](https://assets-docs.dify.ai/2025/03/066cb8eaa89f6ec17aacd8b09f06771c.png)

details\_page

![start_labeling](https://assets-docs.dify.ai/2025/03/4806c56e324589e1711c407f6a1443de.png)

start\_labeling

**Add Metadata** To add a single document’s metadata fields and values:
1. Click **+Add Metadata** to:
![add_metadata](https://assets-docs.dify.ai/2025/03/f9ba9b10bbcf6eaca787eed4fcde44da.png)

add\_metadata

- Create new fields via **+New Metadata**.

> New fields are automatically added to the knowledge base.

![new_fields](https://assets-docs.dify.ai/2025/03/739e7e51436259fca45d16065509fabb.png)

new\_fields

- Add existing fields from the dropdown or from the search box.
![existing_fields](https://assets-docs.dify.ai/2025/03/5b1876e8bc2c880b3b774c97eba371ab.png)

existing\_fields

- Access the Metadata Panel via **Manage**.
![manage_metadata](https://assets-docs.dify.ai/2025/03/8dc74a1d2cdd87294e58dbc3d6dd161b.png)

manage\_metadata

1. *(Optional)* Enter values for new fields.
![values_for_fields](https://assets-docs.dify.ai/2025/03/488107cbea73fd4583e043234fe2fd2e.png)

values\_for\_fields

1. Click **Save** to apply changes.
**Edit Metadata** To update a single document’s metadata fields and values:
1. Click **Edit** in the top right to begin editing.
![edit_mode](https://assets-docs.dify.ai/2025/03/bb33a0f9c6980300c0f979f8dc0d274d.png)
1. Edit metadata:
	- **Update Values:** Type directly in value fields or delete it.
	> Note: You can only modify the value, not the value name.
	- **Delete Fields:** Click the delete icon.
	> Note: This only deletes the field from this document, not from your knowledge base.
![edit_metadata](https://assets-docs.dify.ai/2025/03/4c0c4d83d3ad240568f316abfccc9c2c.png)

edit\_metadata

1. Click **Save** to apply changes.
See **Metadata Filtering** in *[Integrate Knowledge Base within Application](https://docs.dify.ai/en/use-dify/knowledge/integrate-knowledge-within-application)*.

## API Documentation

See *[Maintaining Dataset via API](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-dataset-via-api)*.

## FAQ

- **What can I do with metadata?**
	- Find information faster with smart filtering.
	- Control access to sensitive content.
	- Organize data more effectively.
	- Automate workflows based on metadata rules.
- **Fields vs Values: What is the difference?**
- **How do different delete options work?**

[Previous](https://docs.dify.ai/en/use-dify/knowledge/manage-knowledge/maintain-dataset-via-api)[Integrate Knowledge Base within Application](https://docs.dify.ai/en/use-dify/knowledge/integrate-knowledge-within-application)

[

Next

](https://docs.dify.ai/en/use-dify/knowledge/integrate-knowledge-within-application)
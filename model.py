{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "model.py",
      "provenance": [],
      "mount_file_id": "1KTNTtJHi1h8Bl54SFiF86HobSKSCkhn9",
      "authorship_tag": "ABX9TyOPJF3TjsOppHwCdyKo5BzX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jyotidabass/Binary-classification-preprocessed-tongue-images-with-confidence-score/blob/main/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cNKbpsCE1Qkm"
      },
      "outputs": [],
      "source": [
        "base_dir = '/content/drive/MyDrive/Two-class-cropped/Train'\n",
        "train_directory = '/content/drive/MyDrive/Two-class-cropped/Train'\n",
        "test_directory = '/content/drive/MyDrive/Two-class-cropped/Train'\n",
        "validation_directory = '/content/drive/MyDrive/Two-class-cropped/Train'"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from keras.preprocessing.image import ImageDataGenerator"
      ],
      "metadata": {
        "id": "GeHP7xLt1Xv3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "datagen = ImageDataGenerator(rescale = 1./255)\n",
        "train_generator = datagen.flow_from_directory(train_directory,\n",
        "                                              target_size = (150,150),\n",
        "                                              batch_size = 20,\n",
        "                                              class_mode = 'binary')\n",
        "\n",
        "validation_generator = datagen.flow_from_directory(validation_directory,\n",
        "                                              target_size = (150,150),\n",
        "                                              batch_size = 20,\n",
        "                                              class_mode = 'binary')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MCS5G3L71d0M",
        "outputId": "397795b1-1bcc-4628-fcbe-cb3297f25ccc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 353 images belonging to 2 classes.\n",
            "Found 353 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pathlib\n",
        "data_dir = pathlib.Path(train_directory)"
      ],
      "metadata": {
        "id": "Yp805Wc-1fI6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf \n",
        "train_ds=tf.keras.utils.image_dataset_from_directory(data_dir)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4RckRHVW1kGp",
        "outputId": "f2fa5412-30ee-4b2a-cb30-ee7a0f9fc61f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 353 files belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class_names =train_ds.class_names\n",
        "print(class_names)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w-uom3pf1oUk",
        "outputId": "30079280-b7e1-42e4-f6f0-2657302c6f90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Coated tongue', 'Non-coated tongue']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_classes=len(class_names)"
      ],
      "metadata": {
        "id": "xnA_RzEf1rn6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ffI4mO7c1vCa",
        "outputId": "8cf85af6-22fa-427d-d74c-58178364619a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from keras import layers\n",
        "from keras import models"
      ],
      "metadata": {
        "id": "VDAHR_0912rt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = models.Sequential()\n",
        "#First convolutional layer with 32 3x3 filters\n",
        "model.add(layers.Conv2D(32, (3, 3), activation='relu',\n",
        "      input_shape=(150, 150, 3)))\n",
        "model.add(layers.MaxPooling2D((2, 2)))\n",
        "\n",
        "#Second convolutional layer with 64 3x3 filters\n",
        "model.add(layers.Conv2D(64, (3, 3), activation='relu'))\n",
        "model.add(layers.MaxPooling2D((2, 2)))\n",
        "\n",
        "#Third convolutional layer with 128 3x3 filters\n",
        "model.add(layers.Conv2D(128, (3, 3), activation='relu'))\n",
        "model.add(layers.MaxPooling2D((2, 2)))\n",
        "\n",
        "#Fourth convolutional layer with 128 3x3 filters\n",
        "model.add(layers.Conv2D(128, (3, 3), activation='relu'))\n",
        "model.add(layers.MaxPooling2D((2, 2)))\n",
        "\n",
        "#Fifth convolutional layer with 128 3x3 filters\n",
        "model.add(layers.Conv2D(128, (3, 3), activation='relu'))\n",
        "model.add(layers.MaxPooling2D((2, 2)))\n",
        "\n",
        "#We flatten our final feature map and add a hidden dense layer with 512 neurons\n",
        "model.add(layers.Flatten())\n",
        "model.add(layers.Dense(512, activation='relu'))\n",
        "\n",
        "#Our output layer\n",
        "model.add(layers.Dense(1, activation='sigmoid'))"
      ],
      "metadata": {
        "id": "WSlDp4Eo1yp2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ezrg_IFh2DQI",
        "outputId": "b77288c0-e0c3-4ad7-c5f1-7457635d5e07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " conv2d (Conv2D)             (None, 148, 148, 32)      896       \n",
            "                                                                 \n",
            " max_pooling2d (MaxPooling2D  (None, 74, 74, 32)       0         \n",
            " )                                                               \n",
            "                                                                 \n",
            " conv2d_1 (Conv2D)           (None, 72, 72, 64)        18496     \n",
            "                                                                 \n",
            " max_pooling2d_1 (MaxPooling  (None, 36, 36, 64)       0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_2 (Conv2D)           (None, 34, 34, 128)       73856     \n",
            "                                                                 \n",
            " max_pooling2d_2 (MaxPooling  (None, 17, 17, 128)      0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_3 (Conv2D)           (None, 15, 15, 128)       147584    \n",
            "                                                                 \n",
            " max_pooling2d_3 (MaxPooling  (None, 7, 7, 128)        0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_4 (Conv2D)           (None, 5, 5, 128)         147584    \n",
            "                                                                 \n",
            " max_pooling2d_4 (MaxPooling  (None, 2, 2, 128)        0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " flatten (Flatten)           (None, 512)               0         \n",
            "                                                                 \n",
            " dense (Dense)               (None, 512)               262656    \n",
            "                                                                 \n",
            " dense_1 (Dense)             (None, 1)                 513       \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 651,585\n",
            "Trainable params: 651,585\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from keras import optimizers"
      ],
      "metadata": {
        "id": "Qf2LFQix2IiL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow import keras\n",
        "from keras import optimizers\n",
        "model.compile(loss='binary_crossentropy',\n",
        "optimizer=keras.optimizers.RMSprop(learning_rate=1e-4),\n",
        "metrics=['acc'])"
      ],
      "metadata": {
        "id": "5mZzEOlH2M45"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "result = model.fit(\n",
        "train_generator,\n",
        "steps_per_epoch=10,\n",
        "epochs=4,\n",
        "validation_data=validation_generator,\n",
        "validation_steps=5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "exgAuHA-2Q1F",
        "outputId": "b8de197a-7c69-4acd-aed5-ac28d4c40708"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/4\n",
            "10/10 [==============================] - 63s 6s/step - loss: 0.6592 - acc: 0.6788 - val_loss: 0.6069 - val_acc: 0.7400\n",
            "Epoch 2/4\n",
            "10/10 [==============================] - 27s 3s/step - loss: 0.6592 - acc: 0.6373 - val_loss: 0.6709 - val_acc: 0.6100\n",
            "Epoch 3/4\n",
            "10/10 [==============================] - 24s 2s/step - loss: 0.6513 - acc: 0.6500 - val_loss: 0.6189 - val_acc: 0.7000\n",
            "Epoch 4/4\n",
            "10/10 [==============================] - 18s 2s/step - loss: 0.6436 - acc: 0.6650 - val_loss: 0.6452 - val_acc: 0.6600\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "irtCAa0d2Utw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "acc = result.history['acc']\n",
        "loss = result.history['loss']\n",
        "validation_acc = result.history['val_acc']\n",
        "validation_loss = result.history['val_loss']\n",
        "\n",
        "x = range(1,len(acc)+1)\n",
        "\n",
        "plt.plot(x,acc,'x-b',label = 'Training Accuracy')\n",
        "plt.plot(x,validation_acc,'o-m',label = 'Validation Accuracy')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Accuracy')\n",
        "plt.legend()\n",
        "plt.figure()\n",
        "plt.plot(x,loss,'x-b',label = 'Training Loss')\n",
        "plt.plot(x,validation_loss,'o-m',label = 'Validation Loss')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 541
        },
        "id": "RZ3FzcCu2ZGv",
        "outputId": "dab37d1c-9732-453f-da35-8e5802b999e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEGCAYAAAB/+QKOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdd3zU9f3A8df7skMYCRuy2WEkgbCcuHGBE8GJts6qBetAEUGQatVatY4WrbMqolWLLWodOH4ywxBJ2MllMEOAQMjOfX5/fC+QQCCX5C53Sd7PxyMPuO98f7lw7/tsMcaglFJKHcvm7QCUUkr5Jk0QSimlaqUJQimlVK00QSillKqVJgillFK18vd2AO7SqVMnExsb6+0wlFKqWVm1atVeY0zn2va1mAQRGxtLamqqt8NQSqlmRUSyTrRPq5iUUkrVShOEUkqpWmmCUEopVasW0wahlDqqvLyc3NxcSkpKvB2K8hHBwcFERkYSEBDg8jmaIJRqgXJzc2nbti2xsbGIiLfDUV5mjCE/P5/c3Fzi4uJcPs+jVUwiMlZENonIVhGZVsv+v4jIWufPZhE5cMz+diKSKyIveSrG3e/tZmnsUr63fc/S2KXsfm+3p26lVJMpKSmhY8eOmhwUACJCx44d612i9FgJQkT8gJeB84BcYKWILDTGpFcdY4yZWu34e4DkYy4zB/jRUzHufm83m27bhKPIAUBpVimbbtsEQNfrunrqtko1CU0OqrqG/D54sgQxAthqjMkwxpQB84HxJzl+EvBB1QsRGQZ0Bf7nqQAzpmccSQ5VHEUOMqZneOqWSinVbHgyQfQEcqq9znVuO46IxABxwHfO1zbgz8D9J7uBiNwmIqkikpqXl1fvAEuzS+u1XSnlmvz8fJKSkkhKSqJbt2707NnzyOuysrKTnpuamsq9995b5z1OOeUUd4ULwJQpU+jZsycOh6Pug1sJX+nmOhH42BhT6Xx9F7DIGJN7spOMMfOMMSnGmJTOnWsdKX5SQdFB9dquVEv09NOweHHNbYsXW9sbqmPHjqxdu5a1a9dyxx13MHXq1COvAwMDqaioOOG5KSkpvPjii3XeY8mSJQ0P8BgOh4NPP/2UqKgofvjhB7dd91gne25f5MkEsR2IqvY60rmtNhOpVr0EjAbuFhE78Cxwo4g85e4A4+fGYwut+U9gC7URPzfe3bdSymcNHw4TJhxNEosXW6+HD3fvfSZPnswdd9zByJEjefDBB1mxYgWjR48mOTmZU045hU2brPa/77//nksuuQSAWbNmccsttzBmzBji4+NrJI6wsLAjx48ZM4arrrqK/v37c91111G1UuaiRYvo378/w4YN49577z1y3WN9//33DBw4kDvvvJMPPjj6UbR7924uv/xyEhMTSUxMPJKU3nnnHYYMGUJiYiI33HDDkef7+OOPa43v9NNPZ9y4cSQkJABw2WWXMWzYMAYOHMi8efOOnPPll18ydOhQEhMTOeecc3A4HPTp04eqGhKHw0Hv3r1pSI1JQ3iym+tKoI+IxGElhonAtcceJCL9gXBgadU2Y8x11fZPBlKMMcf1gmqsqobojOkZlGZZ1UrR06O1gVq1KFOmwNq1Jz+mRw+44ALo3h127oQBA+Dxx62f2iQlwfPP1z+W3NxclixZgp+fHwcPHuSnn37C39+fb775hkceeYR//etfx52zceNGFi9ezKFDh+jXrx933nnncX3516xZQ1paGj169ODUU0/l559/JiUlhdtvv50ff/yRuLg4Jk2adMK4PvjgAyZNmsT48eN55JFHKC8vJyAggHvvvZczzzyTTz/9lMrKSgoLC0lLS+OJJ55gyZIldOrUiX379tX53KtXr2b9+vVHupi+8cYbREREUFxczPDhw7nyyitxOBzceuutR+Ldt28fNpuN66+/nvfee48pU6bwzTffkJiYSENqTBrCYyUIY0wFcDfwFbABWGCMSROR2SIyrtqhE4H5xkuLY3e9riuj7aM5df+p+Hfw59CyQ94IQymvCg+3kkN2tvVneLhn7nP11Vfj5+cHQEFBAVdffTWDBg1i6tSppKWl1XrOxRdfTFBQEJ06daJLly7s3n18V/QRI0YQGRmJzWYjKSkJu93Oxo0biY+PP/KhfKIEUVZWxqJFi7jsssto164dI0eO5KuvvgLgu+++48477wTAz8+P9u3b891333H11VfTqVMnACIiIup87hEjRtQYf/Diiy+SmJjIqFGjyMnJYcuWLSxbtowzzjjjyHFV173lllt45513ACux3HzzzXXez108OlDOGLMIWHTMtseOeT2rjmu8Bbzl5tCOE9AhgKgHosicnsnBFQdpN6Kdp2+pVJNw5Zt+VbXSjBnw6qswcyac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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train_datagen = ImageDataGenerator(rescale = 1./255,\n",
        "                                   horizontal_flip = True,\n",
        "                                   rotation_range = 40,\n",
        "                                   width_shift_range = 0.2,\n",
        "                                   height_shift_range = 0.2,\n",
        "                                   shear_range = 0.2,\n",
        "                                   zoom_range = 0.2,\n",
        "                                   fill_mode = 'nearest')"
      ],
      "metadata": {
        "id": "QulW2RDB2cs3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_generator_with_aug = train_datagen.flow_from_directory(train_directory,\n",
        "                                                    batch_size = 20,\n",
        "                                                    target_size = (150,150),\n",
        "                                                    class_mode = 'binary')\n",
        "\n",
        "validation_generator = datagen.flow_from_directory(validation_directory,\n",
        "                                                   batch_size = 20,\n",
        "                                                   target_size = (150,150),\n",
        "                                                   class_mode = 'binary')\n",
        "\n",
        "result_aug = model.fit(train_generator_with_aug,\n",
        "                       steps_per_epoch = 10,\n",
        "                       epochs =4,\n",
        "                       validation_data = validation_generator,\n",
        "                       validation_steps = 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6jh4pktp2jGa",
        "outputId": "6de63e9b-2c10-4b1f-fc4b-7c18653d39eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 353 images belonging to 2 classes.\n",
            "Found 353 images belonging to 2 classes.\n",
            "Epoch 1/4\n",
            "10/10 [==============================] - 18s 2s/step - loss: 0.6484 - acc: 0.6580 - val_loss: 0.6271 - val_acc: 0.6900\n",
            "Epoch 2/4\n",
            "10/10 [==============================] - 19s 2s/step - loss: 0.6464 - acc: 0.6632 - val_loss: 0.6597 - val_acc: 0.6300\n",
            "Epoch 3/4\n",
            "10/10 [==============================] - 18s 2s/step - loss: 0.6468 - acc: 0.6580 - val_loss: 0.6627 - val_acc: 0.6300\n",
            "Epoch 4/4\n",
            "10/10 [==============================] - 20s 2s/step - loss: 0.6605 - acc: 0.6500 - val_loss: 0.6266 - val_acc: 0.6900\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc = result_aug.history['acc']\n",
        "loss = result_aug.history['loss']\n",
        "validation_acc = result_aug.history['val_acc']\n",
        "validation_loss = result_aug.history['val_loss']\n",
        "\n",
        "x = range(1,len(acc)+1)\n",
        "\n",
        "plt.plot(x,acc,'x-b',label = 'Training Accuracy')\n",
        "plt.plot(x,validation_acc,'o-m',label = 'Validation Accuracy')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Accuracy')\n",
        "plt.legend()\n",
        "plt.figure()\n",
        "plt.plot(x,loss,'x-b',label = 'Training Loss')\n",
        "plt.plot(x,validation_loss,'o-m',label = 'Validation Loss')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 541
        },
        "id": "rADGwTvt2oEu",
        "outputId": "bd3ae709-28b8-4390-c63d-d62049944d7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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uXIlF110EatXr+bVV18FIDAwkD59+vDqq69yxRVXEBsbC0BMTEyL+z1x4sQG1x88/fTTvPPOOwBkZ2fzzTffUFBQwNlnn328XN373njjjcyYMYO77rqLF198kR/96Ectfp7yneqiarKfyKbfxf0Y/e5on32OTxsijTErgBWNts31uG+AX7hvnmUqsEYydZrgvsEk3ZtExkMZHP3iKL0n9u7Mj+/2WvNNv65Zac4ceO45mDevYZ9ER4mIiDh+f86cOUybNo133nkHp9PJ1KlTvb4mJKS+XTcwMJCamhO/r7SmTFNWrlzJkSNHGD3a+mcvKysjLCysyeaopgQFBR3v4Ha5XA064z33e+3atXz88cesX7+e8PBwpk6d2uz1CUlJScTFxbF69Wq++OILXnvttZOKS3WsnCdzqC2uJXWhby841LmYPCTcmUBwbDAZczPsDqXHqUsOS5fCwoXWT88+CV8pLi4mIcEaXPfyyy93+PsPHz6cffv24XQ6AXjzzTe9lnvjjTd44YUXcDqdOJ1OMjIy+OijjygrK+O8887jueeeA6C2tpbi4mLOPfdc/vGPf1BYWAhwvInJ4XCwZcsWAJYvX95kjai4uJjo6GjCw8PZvXs3GzZsAGDy5MmsW7eOjIyMBu8L8OMf/5hrrrmmQQ1Mdb6qQ1XkPJVD/yv6E5kW6dPP0gThISgyiKRfJVG0sogj/zlidzg9yqZNVlKoqzFMm2Y93rTJt59733338cADDzB27NiT+sbfWmFhYfzpT39i+vTpjB8/nqioKPr06dOgTFlZGR9++CEXXnjh8W0RERGceeaZvPfee/zhD39gzZo1jB49mvHjx7Nz505GjRrFQw89xDnnnENaWhq/+IVVCb/55pv55JNPSEtLY/369Q1qDZ6mT59OTU0Np556Kvfffz+TJ08GoH///ixevJjLLruMtLQ0rryyfhKDiy++mNLSUm1esln249nUHqvFMd/h88+SupEWXV16errpiAWDastq2XjKRsKGhzFmzRi98rMddu3axamnnmp3GLYrLS0lMjISYww//elPGTp0KHfffbfdYZ20zZs3c/fdd/Ppp5+2633076LtKg9UsnHwRvrP7M+pf+uY36GIbDHGeB3TrTWIRgLDA0l+MJniT4o5slprEar9nn/+ecaMGcOoUaMoLi7m1ltvtTukk/ab3/yGmTNn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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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/FlPepzZg7z5edRV1Hn99TRxtEHpf0opebuElHtTCO0b2voOylbFi4v5wvEFqwJW8YXjC4oXF5/Q8caNG8eKFSuOKnvyySe5+eabW9xn7Nix1HcBP++885qd82n27NksXLjwmK+9bNkytmw5Mr3bzJkz+eijj9oTfrN0+vXORURIm5dG9c5qdjyzw+uvp4mjFabOkD0lm9DUUJKmJLW+g7JV8eJitt6wlaq8KjBQlVfF1hu2nlDymDBhwvdmiF2yZEmbJxp87733jnsQXdPEMXfuXH76058e17FU5xb942iifxJN/oJ8ag95d5oYTRwtqP/W+knQJxzecJiYX8QQGBZod1hd3rbJ2/h67Nct3r699ltc5UdfIHSVu/j22m9b3Gfb5G3HfM1f/vKXvPvuuw2LNjmdTnbs2MGZZ57JzTffTGZmJieffDKzZs1qdn+Hw8HevdacQvPnz2fAgAH88Ic/ZOvWrQ3bPP/884waNYpTTz2Vyy67jPLycj7//HOWL1/OXXfdxbBhw9i+fTuTJk3irbfeAqwR4sOHD2fIkCFcc801VFVVNbzerFmzGDFiBEOGDOHbb79t8+/3jTfeYMiQIZxyyilMmzYNgLq6OiZNmsQpp5zCkCFDeOKJJwB46qmnOOmkkxg6dChXXHFFm19DeU/avDRq9tRQ9LR3Z2LSxNGMo761uu36y64TbvJQ3meqmp9EoKXytujVqxejR4/m/fet2fuXLFnC+PHjERHmz59PVlYWGzZs4JNPPmHDhg0tHmfNmjUsWbKEdevW8d5777G60QRal156KatXr2b9+vUMHjyYF198kR/84AdceOGFPProo6xbt46MjCNr2VdWVjJp0iTefPNNNm7cSG1tLc8880zD871792bt2rXcfPPNrTaH1auffv0///kP69atY/Xq1Sxbtox169Y1TL++ceNGrr76asCafv3rr79mw4YNPPvss+36nSrv6HFGD3qd14uCRwqoPeC9Wocmjmbk3JfT7LfWnPtybIpI1ev/ZH+Grxre4i00tflrUKGpoS3u0//J/s3u01jj5qrGzVRLly5lxIgRDB8+nM2bNx/VrNTUf//7Xy655BIiIiLo3r07F154YcNzmzZt4swzz2TIkCEsXryYzZs3HzOerVu3kpaWxoABAwC46qqr+PTTTxuev/TSSwEYOXJkw8SIrWk8/XpQ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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#from tensorflow.keras.applications.vgg16 import VGG\n",
        "from tensorflow.keras.applications import VGG16"
      ],
      "metadata": {
        "id": "TRlLFwp22tmE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "vgg16_base = VGG16(include_top = False,\n",
        "                   weights = 'imagenet',\n",
        "                   input_shape = (150,150,3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tLWZRTBC2x_I",
        "outputId": "01cd4b63-2c77-47fc-d313-15cc22f7c1ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/vgg16/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5\n",
            "58892288/58889256 [==============================] - 0s 0us/step\n",
            "58900480/58889256 [==============================] - 0s 0us/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "vgg16_base.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RBNueawC20cE",
        "outputId": "54503559-f3b7-46c7-8d37-3a78c55a8fb3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"vgg16\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " input_1 (InputLayer)        [(None, 150, 150, 3)]     0         \n",
            "                                                                 \n",
            " block1_conv1 (Conv2D)       (None, 150, 150, 64)      1792      \n",
            "                                                                 \n",
            " block1_conv2 (Conv2D)       (None, 150, 150, 64)      36928     \n",
            "                                                                 \n",
            " block1_pool (MaxPooling2D)  (None, 75, 75, 64)        0         \n",
            "                                                                 \n",
            " block2_conv1 (Conv2D)       (None, 75, 75, 128)       73856     \n",
            "                                                                 \n",
            " block2_conv2 (Conv2D)       (None, 75, 75, 128)       147584    \n",
            "                                                                 \n",
            " block2_pool (MaxPooling2D)  (None, 37, 37, 128)       0         \n",
            "                                                                 \n",
            " block3_conv1 (Conv2D)       (None, 37, 37, 256)       295168    \n",
            "                                                                 \n",
            " block3_conv2 (Conv2D)       (None, 37, 37, 256)       590080    \n",
            "                                                                 \n",
            " block3_conv3 (Conv2D)       (None, 37, 37, 256)       590080    \n",
            "                                                                 \n",
            " block3_pool (MaxPooling2D)  (None, 18, 18, 256)       0         \n",
            "                                                                 \n",
            " block4_conv1 (Conv2D)       (None, 18, 18, 512)       1180160   \n",
            "                                                                 \n",
            " block4_conv2 (Conv2D)       (None, 18, 18, 512)       2359808   \n",
            "                                                                 \n",
            " block4_conv3 (Conv2D)       (None, 18, 18, 512)       2359808   \n",
            "                                                                 \n",
            " block4_pool (MaxPooling2D)  (None, 9, 9, 512)         0         \n",
            "                                                                 \n",
            " block5_conv1 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_conv2 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_conv3 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_pool (MaxPooling2D)  (None, 4, 4, 512)         0         \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 14,714,688\n",
            "Trainable params: 14,714,688\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Freezing the convoutional base\n",
        "vgg16_base.trainable = False"
      ],
      "metadata": {
        "id": "IE0EUwmS23So"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "new_model = models.Sequential()\n",
        "new_model.add(vgg16_base)\n",
        "new_model.add(layers.Flatten())\n",
        "new_model.add(layers.Dense(256,activation = 'relu'))\n",
        "new_model.add(layers.Dense(1,activation = 'sigmoid'))"
      ],
      "metadata": {
        "id": "uQt9tRD229Jl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "new_model.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i8rwh8sp3KJp",
        "outputId": "1b0739d1-40b5-4582-bc10-34bc3d7372c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential_1\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " vgg16 (Functional)          (None, 4, 4, 512)         14714688  \n",
            "                                                                 \n",
            " flatten_1 (Flatten)         (None, 8192)              0         \n",
            "                                                                 \n",
            " dense_2 (Dense)             (None, 256)               2097408   \n",
            "                                                                 \n",
            " dense_3 (Dense)             (None, 1)                 257       \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 16,812,353\n",
            "Trainable params: 2,097,665\n",
            "Non-trainable params: 14,714,688\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_model.compile(optimizer = keras.optimizers.RMSprop( learning_rate= 2e-5),\n",
        "                  loss = 'binary_crossentropy',\n",
        "                  metrics = 'acc')"
      ],
      "metadata": {
        "id": "BDN4V4_e3NAf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_datagen = ImageDataGenerator(rescale = 1./255,\n",
        "                                   horizontal_flip = True,\n",
        "                                   rotation_range = 40,\n",
        "                                   width_shift_range = 0.2,\n",
        "                                   height_shift_range = 0.2,\n",
        "                                   shear_range = 0.2,\n",
        "                                   zoom_range = 0.2,\n",
        "                                   fill_mode = 'nearest')\n",
        "\n",
        "train_generator_vgg16 = train_datagen.flow_from_directory(train_directory, \n",
        "                                                          target_size = (150,150),\n",
        "                                                          batch_size = 20,\n",
        "                                                          class_mode = 'binary')\n",
        "\n",
        "validation_generator = datagen.flow_from_directory(validation_directory,\n",
        "                                                   target_size = (150,150),\n",
        "                                                   batch_size = 20,\n",
        "                                                   class_mode = 'binary')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nu-nQmiw3Qw5",
        "outputId": "58928fc5-595b-47c4-bddc-fe461211d85d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 353 images belonging to 2 classes.\n",
            "Found 353 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result_vgg16 = new_model.fit(train_generator_vgg16,\n",
        "                       steps_per_epoch = 10,\n",
        "                       epochs =4,\n",
        "                       validation_data = validation_generator,\n",
        "                       validation_steps = 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QuHNfXKZ3VKj",
        "outputId": "207d2a7f-78b6-4692-b286-f7db31b02098"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/4\n",
            "10/10 [==============================] - 79s 8s/step - loss: 0.6769 - acc: 0.6450 - val_loss: 0.6945 - val_acc: 0.5900\n",
            "Epoch 2/4\n",
            "10/10 [==============================] - 79s 8s/step - loss: 0.6410 - acc: 0.6850 - val_loss: 0.6958 - val_acc: 0.5900\n",
            "Epoch 3/4\n",
            "10/10 [==============================] - 70s 7s/step - loss: 0.6760 - acc: 0.6200 - val_loss: 0.6400 - val_acc: 0.6600\n",
            "Epoch 4/4\n",
            "10/10 [==============================] - 85s 9s/step - loss: 0.6596 - acc: 0.6250 - val_loss: 0.6190 - val_acc: 0.6700\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc = result_vgg16.history['acc']\n",
        "loss = result_vgg16.history['loss']\n",
        "validation_acc = result_vgg16.history['val_acc']\n",
        "validation_loss = result_vgg16.history['val_loss']\n",
        "\n",
        "x = range(1,len(acc)+1)\n",
        "\n",
        "plt.plot(x,acc,'x-b',label = 'Training Accuracy')\n",
        "plt.plot(x,validation_acc,'o-m',label = 'Validation Accuracy')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Accuracy')\n",
        "plt.legend()\n",
        "plt.figure()\n",
        "plt.plot(x,loss,'x-b',label = 'Training Loss')\n",
        "plt.plot(x,validation_loss,'o-m',label = 'Validation Loss')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 541
        },
        "id": "Rign7Ttn3m4y",
        "outputId": "b5de0186-ee80-47f3-ff31-f319a68e7b0c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "vgg16_base.trainable = True\n",
        "for layer in vgg16_base.layers:\n",
        "  if layer.name == 'block5_conv1':\n",
        "    break\n",
        "  layer.trainable = False"
      ],
      "metadata": {
        "id": "bxMfnHWQ3r2z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "vgg16_base.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U4WAOb4V3va7",
        "outputId": "b5ea5e3b-69e4-4444-9c97-9f0c7514dc8f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"vgg16\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " input_1 (InputLayer)        [(None, 150, 150, 3)]     0         \n",
            "                                                                 \n",
            " block1_conv1 (Conv2D)       (None, 150, 150, 64)      1792      \n",
            "                                                                 \n",
            " block1_conv2 (Conv2D)       (None, 150, 150, 64)      36928     \n",
            "                                                                 \n",
            " block1_pool (MaxPooling2D)  (None, 75, 75, 64)        0         \n",
            "                                                                 \n",
            " block2_conv1 (Conv2D)       (None, 75, 75, 128)       73856     \n",
            "                                                                 \n",
            " block2_conv2 (Conv2D)       (None, 75, 75, 128)       147584    \n",
            "                                                                 \n",
            " block2_pool (MaxPooling2D)  (None, 37, 37, 128)       0         \n",
            "                                                                 \n",
            " block3_conv1 (Conv2D)       (None, 37, 37, 256)       295168    \n",
            "                                                                 \n",
            " block3_conv2 (Conv2D)       (None, 37, 37, 256)       590080    \n",
            "                                                                 \n",
            " block3_conv3 (Conv2D)       (None, 37, 37, 256)       590080    \n",
            "                                                                 \n",
            " block3_pool (MaxPooling2D)  (None, 18, 18, 256)       0         \n",
            "                                                                 \n",
            " block4_conv1 (Conv2D)       (None, 18, 18, 512)       1180160   \n",
            "                                                                 \n",
            " block4_conv2 (Conv2D)       (None, 18, 18, 512)       2359808   \n",
            "                                                                 \n",
            " block4_conv3 (Conv2D)       (None, 18, 18, 512)       2359808   \n",
            "                                                                 \n",
            " block4_pool (MaxPooling2D)  (None, 9, 9, 512)         0         \n",
            "                                                                 \n",
            " block5_conv1 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_conv2 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_conv3 (Conv2D)       (None, 9, 9, 512)         2359808   \n",
            "                                                                 \n",
            " block5_pool (MaxPooling2D)  (None, 4, 4, 512)         0         \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 14,714,688\n",
            "Trainable params: 7,079,424\n",
            "Non-trainable params: 7,635,264\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_model.compile(loss='binary_crossentropy',\n",
        "optimizer=keras.optimizers.RMSprop(learning_rate=1e-5),\n",
        "metrics='acc')"
      ],
      "metadata": {
        "id": "iQKZTkgj3xwi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "result_fine_tune = new_model.fit(train_generator_vgg16,\n",
        "                                 steps_per_epoch = 10,\n",
        "                                 epochs = 4,\n",
        "                                 validation_data = validation_generator,\n",
        "                                 validation_steps = 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-YjVhm4l31Q-",
        "outputId": "94e18988-0876-4569-d79b-b7a0a4e5f3ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/4\n",
            "10/10 [==============================] - 82s 8s/step - loss: 0.6383 - acc: 0.6684 - val_loss: 0.5792 - val_acc: 0.6900\n",
            "Epoch 2/4\n",
            "10/10 [==============================] - 81s 8s/step - loss: 0.6137 - acc: 0.6800 - val_loss: 0.6081 - val_acc: 0.6800\n",
            "Epoch 3/4\n",
            "10/10 [==============================] - 81s 8s/step - loss: 0.6065 - acc: 0.6684 - val_loss: 0.5750 - val_acc: 0.7100\n",
            "Epoch 4/4\n",
            "10/10 [==============================] - 80s 8s/step - loss: 0.6188 - acc: 0.6700 - val_loss: 0.6183 - val_acc: 0.6700\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc = result_fine_tune.history['acc']\n",
        "loss = result_fine_tune.history['loss']\n",
        "validation_acc = result_fine_tune.history['val_acc']\n",
        "validation_loss = result_fine_tune.history['val_loss']\n",
        "\n",
        "x = range(1,len(acc)+1)\n",
        "\n",
        "plt.plot(x,acc,'x-b',label = 'Training Accuracy')\n",
        "plt.plot(x,validation_acc,'o-m',label = 'Validation Accuracy')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Accuracy')\n",
        "plt.legend()\n",
        "plt.figure()\n",
        "plt.plot(x,loss,'x-b',label = 'Training Loss')\n",
        "plt.plot(x,validation_loss,'o-m',label = 'Validation Loss')\n",
        "plt.xlabel('Epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 541
        },
        "id": "Lu4uFzPE330Z",
        "outputId": "7fad85e5-aa0b-4c18-e753-81c63d563c06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEGCAYAAAB/+QKOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeVzUdf7A8debQ1DxQMUTFVRAUS5FzaxNatssW90OTdPK2s4tu7b7zvK31drldlqblZlm7ebaZlmZpWtWHoHKoSIi4IGKiCf35/fHZ1REVNQZZhjez8eDhzPf+X5n3l8H5j2f7/tziDEGpZRSqjofdweglFLKM2mCUEopVSNNEEoppWqkCUIppVSNNEEopZSqkZ+7A3CWNm3amLCwMHeHoZRS9cqKFSt2GmNCanrMaxJEWFgYy5cvd3cYSilVr4jIpuM95tJLTCIyVETWikimiDx0nH1GiUiaiKSKyMfVHmsuInki8por41RKKXUsl7UgRMQXeB24EMgDlonIXGNMWpV9IoCHgcHGmEIRaVvtaZ4BFrkqRqWUUsfnyhbEACDTGJNljCkFZgEjqu1zE/C6MaYQwBiz/dADItIPaAd848IYlVJKHYcraxCdgNwq9/OAgdX2iQQQkSWAL/CUMeZrEfEBXgTGAb8/3guIyM3AzQBdunRxXuRKqRMqKysjLy+P4uJid4eiaikwMJDQ0FD8/f1rfYy7i9R+QAQwBAgFFolIDDYxzDPG5InIcQ82xkwFpgIkJibqpFJK1ZG8vDyaNWtGWFgYJ/obVZ7BGENBQQF5eXmEh4fX+jhXXmLaDHSucj/Usa2qPGCuMabMGLMRWIdNGIOAO0QkG5gMXCsizzk7wBdegIULj962cKHdrpQ6vuLiYlq3bq3JoZ4QEVq3bn3KLT5XJohlQISIhItII2A0MLfaPnOwrQdEpA32klOWMWasMaaLMSYMuA/40BhTYy+oM9G/P4wadSRJLFxo7/fv7+xXUsr7aHKoX07n/XJZgjDGlAN3APOBdGC2MSZVRCaKyHDHbvOBAhFJAxYC9xtjClwVU3VJSTBrFgwbBhMm2OQwe7bdrpRSDZ1Lx0EYY+YZYyKNMd2NMZMc254wxsx13DbGmHuNMdHGmBhjzKwanuN9Y8wdroqxc2eorITXXrOJQZODUp6voKCA+Ph44uPjad++PZ06dTp8v7S09ITHLl++nDvvvPOkr3H22Wc7JdYffviBSy+91CnPVdfcXaR2u82boWlTaN0aPv0URo6EGTOgUSN3R6aUd3jhBXvZtuqXr4ULYdkyeOCB03vO1q1bk5ycDMBTTz1FUFAQ99133+HHy8vL8fOr+eMtMTGRxMTEk77GTz/9dHrBeZEGPVnfoZrDZ59BVhZcdpm9HR8POTnujk4p71BXtb7x48dz6623MnDgQB544AF+/fVXBg0aREJCAmeffTZr164Fjv5G/9RTT3HDDTcwZMgQunXrxpQpUw4/X1BQ0OH9hwwZwpVXXknPnj0ZO3Ysh1binDdvHj179qRfv37ceeedp9RSmDlzJjExMfTp04cHH3wQgIqKCsaPH0+fPn2IiYnh5ZdfBmDKlClER0cTGxvL6NGjz/w/q5YadAti2bKjaw7//jc8+SQ89xwkJMD06XDJJe6NUSlPd/fd4Pgyf1wdO8JFF0GHDrB1K/TqBU8/bX9qEh8Pr7xy6rHk5eXx008/4evry549e1i8eDF+fn589913PPLII/zrX/865piMjAwWLlzI3r17iYqK4rbbbjtmrMBvv/1GamoqHTt2ZPDgwSxZsoTExERuueUWFi1aRHh4OGPGjKl1nFu2bOHBBx9kxYoVBAcH84c//IE5c+bQuXNnNm/ezJo1awDYvXs3AM899xwbN24kICDg8La60KBbEA88cGzN4emnYc0aW5sYNgweeQTKy90Tn1LeIjjYJoecHPtvcLBrXmfkyJH4+voCUFRUxMiRI+nTpw/33HMPqampNR4zbNgwAgICaNOmDW3btiU/P/+YfQYMGEBoaCg+Pj7Ex8eTnZ1NRkYG3bp1Ozyu4FQSxLJlyxgyZAghISH4+fkxduxYFi1aRLdu3cjKymLChAl8/fXXNG/eHIDY2FjGjh3LRx99dNxLZ67QoFsQxxMRAUuXwl13wd/+BkuWwMyZ9luQUupotfmmf+iy0uOPw5tv2pa6KzqENG3a9PDtxx9/nKSkJD7//HOys7MZMmRIjccEBAQcvu3r60t5Dd8Ia7OPMwQHB5OSksL8+fN56623mD17Nu+99x5ffvklixYt4osvvmDSpEmsXr26ThJFg25BnEjjxjB1Knz4ISxfbi85LVjg7qiUqn8OJYfZs2HiRPtv1ZqEqxQVFdGpUycA3n//fac/f1RUFFlZWWRnZwPwySef1PrYAQMG8OOPP7Jz504qKiqYOXMm5513Hjt37qSyspIrrriCZ599lpUrV1JZWUlubi5JSUk8//zzFBUVsW/fPqefT000QZzENdfYWkXr1nDhhfYXvKLC3VEpVX9Ur/UlJdn7y5a59nUfeOABHn74YRISElzyjb9x48a88cYbDB06lH79+tGsWTNatGhR474LFiwgNDT08E92djbPPfccSUlJxMXF0a9fP0aMGMHmzZsZMmQI8fHxjBs3jr/97W9UVFQwbtw4YmJiSEhI4M4776Rly5ZOP5+ayKFqfH2XmJhoXLlg0P79cNtttnB94YXw0UfQtvrk5Eo1EOnp6fTq1cvdYbjdvn37CAoKwhjD7bffTkREBPfcc4+7wzqumt43EVlhjKmx36+2IGqpaVP44AN45x1YvNheclq82N1RKaXc6Z133iE+Pp7evXtTVFTELbfc4u6QnEoTxCkQgRtvhJ9/tgkjKQmef96OxFZKNTz33HMPycnJpKWlMWPGDJo0aeLukJxKE8RpiIuzhevLL4eHHoLhw6GgzmaQUkqpuqEJ4jQ1bw6ffGLncPrmG+jbF375xd1RKaWU82iCOAMicPvtdpyEjw+cey68+ip4Sd1fKdXAaYJwgv79YeVKuPhiO+3AlVdCUZG7o1JKqTOjCcJJgoNhzhyYPBn+8x/o1w9++83dUSnlnZKSkpg/f/5R21555RVuu+224x4zZMgQDnWFv+SSS2qc0+ipp55i8uTJJ3ztOXPmkJaWdvj+E088wXfffXcq4dfIE6cF1wThRCLw17/Cjz9CcTEMGgRvv62XnJTKn5HP0rCl/ODzA0vDlpI/49j5jk7FmDFjmDXr6OVjZs2aVev5kObNm3fag82qJ4iJEyfy+9///rSey9NpgnCBwYNt62HIELj1Vhg3DupoZLxSHid/Rj5rb15LyaYSMFCyqYS1N689oyRx5ZVX8uWXXx5eHCg7O5stW7Zw7rnnctttt5GYmEjv3r158sknazw+LCyMnTt3AjBp0iQiIyM555xzDk8JDnaMQ//+/YmLi+OKK67gwIED/PTTT8ydO5f777+f+Ph4NmzYwPjx4/nss88AO2I6ISGBmJgYbrjhBkpKSg6/3pNPPknfvn2JiYkhIyOj1ufqzmnBdbI+FwkJgXnz7GR/TzxhaxSffgp9+rg7MqWca/3d69mXfPxvQHt+3oMpOboZXXmgkow/Z7DlnS01HhMUH0TEKxHHfc5WrVoxYMAAvvrqK0aMGMGsWbMYNWoUIsKkSZNo1aoVFRUVXHDBBaxatYrY2Ngan2fFihXMmjWL5ORkysvL6du3L/369QPg8ssv56abbgLgscce45///CcTJkxg+PDhXHrppVx55ZVHPVdxcTHjx49nwYIFREZGcu211/Lmm29y9913A9CmTRtWrlzJG2+8weTJk3n33XePe36HuHtacG1BuJCPDzz6KHz3HRQWwoABdjS2Ug1J9eRwsu21VfUyU9XLS7Nnz6Zv374kJCSQmpp61OWg6hYvXsxll11GkyZNaN68OcOHDz/82Jo1azj33HOJiYlhxowZx50u/JC1a9cSHh5OZGQkANdddx2LFi06/Pjll18OQL9+/Q5P8Hcy7p4WXFsQdSApyS6oMmYMjB8PixbBP/4BXjboUjVQJ/qmD7A0bKm9vFRNQNcAEn5IOO3XHTFiBPfccw8rV67kwIED9OvXj40bNzJ58mSWLVtGcHAw48ePp7i4+LSef/z48cyZM4e4uDjef/99fvjhh9OOFY5MGe6M6cLralpwbUHUkfbtbUviscdg2jQ46yyocrlTKa/VbVI3fJoc/VHj08SHbpO6ndHzBgUFkZSUxA033HC49bBnzx6aNm1KixYtyM/P56uvvjrhc/zud79jzpw5HDx4kL179/LFF18cfmzv3r106NCBsrIyZsyYcXh7s2bN2Lt37zHPFRUVRXZ2NpmZmQBMnz6d884774zO0d3TgmsLog75+sIzz8A559jCdWKinfyvDpeYVarOtRvbDoCsR7MoySkhoEsA3SZ1O7z9TIwZM4bLLrvs8KWmuLg4EhIS6NmzJ507d2bw4MEnPL5v375cddVVxMXF0bZtW/pXWSj7mWeeYeDAgYSEhDBw4MDDSWH06NHcdNNNTJky5XBxGiAwMJBp06YxcuRIysvL6d+/P7feeuspnc+hacEP+fTTTw9PC26MYdiwYYwYMYKUlBSuv/56Kh0TwVWdFryoqAhjjFOmBXfpdN8iMhR4FfAF3jXGPFfDPqOApwADpBhjrhaRrsDn2BaOP/APY8xbJ3otV0/37Wx5eTYxLFlipxF/6SUIDHR3VErVjk73XT95zHTfIuILvA5cDEQDY0Qkuto+EcDDwGBjTG/gbsdDW4FBxph4YCDwkIh41YKfoaF2Ra3777dLMA4eDFlZ7o5KKaWOcGUNYgCQaYzJMsaUArOAEdX2uQl43RhTCGCM2e74t9QYc6iqFeDiON3G3x9eeMGOvM7KshP+ff65u6NSSinLlR+8nYDcKvfzHNuqigQiRWSJiPzsuCQFgIh0FpFVjud43hhzTIdpEblZRJaLyPIdO3a44BTqxvDhdmBdZKSdQvzee8Ex/kcpj+Utq1E2FKfzfrn7m7kfEAEMAcYA74hISwBjTK4xJhboAVwnIsdUtIwxU40xicaYxJCQkDoM2/nCwuwKdRMmwMsvw3nnQU6Ou6NSqmaBgYEUFBRokqgnjDEUFBQQeIqFTlf2YtoMdK5yP9Sxrao84BdjTBmwUUTWYRPG4eXMjTFbRGQNcC7wGV4sIACmTLHThv/5z3ZZ0+nT4ZJL3B2ZUkcLDQ0lLy+P+txyb2gCAwOP6iFVG65MEMuACBEJxyaG0cDV1faZg205TBORNthLTlkiEgoUGGMOikgwcA7wsgtj9SgjR0J8vP132DB4+GGYOBGcMDBSKafw9/cnPDzc3WEoF3PZJSZjTDlwBzAfSAdmG2NSRWSiiBwazz4fKBCRNGAhcL8xpgDoBfwiIinAj8BkY8xqV8XqiSIiYOlSuOkmO5/TBRfAlpqnrVFKKZdw6TiIulTfxkGciunT7aywQUHw8cc2WSillDO4ZRyEcp5rroFly6B1a7jwQnu5qaLC3VEppbydJoh6IjraJolx4+DJJ+3yptu3uzsqpZQ30wRRjzRtaqcLf+cd2yU2IcH+q5RSrqAJop4RgRtvhJ9/tgkjKQmefx4cc3YppZTTaIKop+LiYPlyO/L6oYfsaOyCAndHpZTyJpog6rHmzeGTT+C11+Cbb+xcTr/84u6olFLeQhNEPScCt99upw338bGjsKdMAS/pvayUciNNEF6if39YuRKGDoW77rKjsIuK3B2VUqo+0wThRYKD7dThkyfDnDnQr5+dJVYppU6HJggvIwJ//Sv8+CMUF8OgQfD223rJSSl16jRBeKnBg23rYcgQO03HuHFwhuuXK6UaGE0QXiwkBObNg2efhVmzbJ1izRp3R6WUqi80QXg5Hx949FH47jsoLIQBA+xobKWUOhlNEA1EUhIkJ8PAgTB+vF2Q6MABd0ellPJkmiAakPbtbUviscdg2jQ46yxYu9bdUSmlPJUmiAbG1xeeeQa++gq2boXERFufUEqp6jRBNFAXXWR7OcXFwZgx8Je/2G6xSil1iCaIBiw0FBYuhPvvhzfftF1js7LcHZVSylNogmjg/P3hhRfsCOysLDvh35w57o5KKeUJNEEowE4XvnIlRETAZZfZ0dhlZe6OSinlTpog1GHh4fC//8GECfDSS/C730FOjrujUkq5iyYIdZSAADtd+OzZkJpqlzWdN8/dUSml3MGlCUJEhorIWhHJFJGHjrPPKBFJE5FUEfnYsS1eRJY6tq0SkatcGac61siRsGIFdO4Mw4bBI49Aebm7o1JK1SWXJQgR8QVeBy4GooExIhJdbZ8I4GFgsDGmN3C346EDwLWObUOBV0SkpatiVTWLiIClS+Gmm+Bvf4MLLoAtW9wdlVKqrriyBTEAyDTGZBljSoFZwIhq+9wEvG6MKQQwxmx3/LvOGLPecXsLsB0IcWGs6jgaN4apU+HDD+0a2AkJsGCBu6NSStUFVyaITkBulft5jm1VRQKRIrJERH4WkaHVn0REBgCNgA0ui1Sd1DXXwLJl0Lo1XHghTJwIFRXujkop5UruLlL7ARHAEGAM8E7VS0ki0gGYDlxvjKmsfrCI3Cwiy0Vk+Y4dO+oo5IYrOtomiXHj4Mkn4eKLYft2d0elVMP0wgt2oGtVCxfa7c7iygSxGehc5X6oY1tVecBcY0yZMWYjsA6bMBCR5sCXwKPGmJ9regFjzFRjTKIxJjEkRK9A1YWmTe104e+8A4sX20tOixe7OyqlGp7+/WHUqCNJYuFCe79/f+e9hisTxDIgQkTCRaQRMBqYW22fOdjWAyLSBnvJKcux/+fAh8aYz1wYozoNInDjjfDzzzZhJCXB889D5TFtPKWUqyQlwcw/57PjgqUslB/Y+fulzL45n6Qk572GyxKEMaYcuAOYD6QDs40xqSIyUUSGO3abDxSISBqwELjfGFMAjAJ+B4wXkWTHT7yrYlWnJy7OFq4vvxweeghGjIBdu9wdlVLeb9UqePHifMqfX0tbU4IAIZUl+L6ylvwZ+U57HTFespp9YmKiWb58ubvDaJCMgddfh3vvhQ4d7CC7gQPdHZVS3mXXLvj4Y7uWy8qVMIultKPkmP0CugYwKHtQrZ9XRFYYYxJreszdRWrlBUTgjjtgyRJ7+9xz7WhsL/nuoZTbVFTYtVtGjbJfviZMsJdyX30V2sqxyQGgOKfm7adDE4Rymv797RoTQ4fCXXfZ0dhFRe6OSqn6Z906ePhh6NIFLrkEvv8ebr3V/n399hvceSeUNWtU47GlLQKcFocmCOVUwcF26vDJk+204f362V9opdSJ7dkD775r12WJioK//91Ov//ZZ3YGg1dfhXhHJbaiuIJmLeWY5/Bp4kP8a92cFpMmCOV0Ina68B9/tKvUDRoEb7+tl5yUqq6y0nZPvfZau2b8TTdBYaEdy5CbC198AVdcAY2qNRY23LuBkpwSQv8aSkDXABBbe4iaGkW7se2cFp+f055JqWoGD7ath2uusc3jRYtsoggKcndkSrlXdrYdT/T++/Z28+Y2SVx/PQwYYL9kHc/2T7az5c0tdL6/M91f6E6PyT1cFqe2IJRLhYTY6cKffRZmzbJ1ijVr3B2VUnXvwAGYPh3OP9+uvfL009CjB8yYAdu2wVtv2d5/J0oOB9YfYO2Na2l+dnPCJ4W7PGZNEMrlfHzg0Ufhu+9s83nAAPvtSSlvZwz89JO9dNS+vW0lbNpk5zLLzoZvv4Wrr7aTYp5MxcEKUkemIo2E6FnR+Pi7/uNbLzGpOpOUBMnJMGYMjB9vLzn94x/QpIm7I1PKubZssTMgv/8+rF1rf8dHjrSXkM49135pOlWZ92SyP2U/Mf+NIbBzoNNjrom2IFSdat/etiQee8wO+DnrLPsHpFR9V1ICn35qu6V27my7qbZtC++9Zy8hvf8+nHfe6SWH/Jn5bH17K50f6EzrYa2dHvvxaIJQdc7XF555xg4A2roVEhPhk0/cHZVSp84Yu/LiHXfYgWyjRsHq1TY5rF9vW8nXXw/Nmp3+axxYe4B1N6+j+eDmhD/r+rpDVXqJSbnNRRfZXk5XXQWjR9s/ppdesutiK+XJduyAjz6yreDVq+3v7GWX2WRwwQX2S5AzVBysIHVUKhJQd3WHqrQFodwqNBR++AHuuw/eeAO6d7e9Oqpy9hz3Sp2OsjKYO9cmgo4d7dxjgYH293brVpg5E/7wB+clB4DMuzLZv2o/vab3IjC0buoOVWkLQrmdv78dNXrOOTB2rB03kZUFjz9+ZI772bPdHaVqqFJTbUvho48gP9/WFe66y7YWevd23evmz8hn6ztb6fJQF1pfXHd1h6p0NlflUTZutHM5rVsHMTG2K+Abb9jEcaL+4Uo5U2GhHbczbZpdRdHPDy691CaFiy+2X2pcaX/GflYkrqBZQjPiFsbh4+e6iz0nms1VE4TyOCUltrfHL78c2RYSYns8DRpkf/r3t4sVKeUsFRWwYIFNCp9/bn8PY2NtUrj6attyqJM4DlSwcuBKSreV0u+3fi6/tHSiBKGXmJTH+ekn2LDBDq574w37B7prFyxdauemAXudNzYWzj77SNIID9dWhjp1mZm2C+oHH0Benp1w8qab7O9dQkLd/05l3pXJ/jX7ifkqxi11h6o0QSiPUrXmkJRke4Qcuj9tGhQU2JbF0qX254MP7GJFYL/hHUoWgwbZ7rM6CE/VZO9eO2Zh2jT43//s2ISLLrK96IYPd19Pum0fbWPru1vp8kgXWg91T92hKr3EpDzKCy/Yy0dV19VduNBeB37ggWP3r6iwRcRDCWPpUlu/AHvdOC7u6KQRFqatjIbKGNuVeto0O4X2/v0QGWlbCtdcA506uTe+/emOukNiM+IWuLbuUJXWIFSDsnMn/PzzkYTx66/2wwCgXbtjWxm1mQdH1V85OUdmTs3KsoPWRo+2070MGuQZXxgO1x3yS0lMTiSgY901YbQGoRqUNm1sj5NLL7X3y8vtDLJVWxlz5tjH/PzsIixVk0bXrp7xoaFO38GDttA8bZotPBtjZ1F9+mm4/HLPu/S4fsJ69qfuJ/br2DpNDiejLQjVIO3YcWwr48AB+1j79kcnjH79tJVRHxhj61Pvv2+7qBYV2UuK48fDddfZ255o24fbyLgugy6PdqHbs85bDa629BKTUidRXm6nTKjaytiwwT7m729bGVV7THXurK0MT7F1q11n4f33IT3dJvMrr7S1hdOdHK+u7E/bz4r+K2jWvxlx39Vd3aEqTRBKnYbt249uZSxbdqSV0bHj0a2Mvn3ttAuqbpSW2i7P06bB11/bzgpnn22TwqhRdoU2T1exv4IVA1ZQtqOszusOVbmtBiEiQ4FXAV/gXWPMczXsMwp4CjBAijHmasf2r4GzgP8ZYy51ZZxK1aRtW9vlcfhwe7+s7NhWxr/+ZR/z97dJomrS6NzZfbF7q+RkmxRmzLBdnjt2hPvvt5eRoqLcHd2pWX/Heg6kHyB2vmfVHapyWQtCRHyBdcCFQB6wDBhjjEmrsk8EMBs43xhTKCJtjTHbHY9dADQBbqlNgtAWhHKH/PyjE8by5bZACrbbZPVWhs5Ue+p27oSPP7aJITkZGjWCESNsa8HZk+PVla3vb2Xt9Wvp+nhXwifW7RTe1bmrBTEAyDTGZDmCmAWMANKq7HMT8LoxphDgUHJw3F4gIkNcGJ9SZ6xdO/jTn+wP2FZGSsrRSeOzz+xjjRod28oIDXVf7J6svBzmz7dJYe5c+//arx+89ppdkbBVK3dHePr2p+5n/V/W03JIS8KeDHN3OCfkygTRCcitcj8PGFhtn0gAEVmCvQz1lDHm69q+gIjcDNwM0KVLlzMKViln8Pe3YysSE2HCBLtt27ajE8abb8LLL9vHQkOPThgJCQ27lZGebpPC9On2/y0kxC7Gc/31dvLG+q5iv11X2reZL70+7oX4enZPB3ePg/ADIoAhQCiwSERijDG7a3OwMWYqMBXsJSZXBanUmWjf3q4hcNll9n5p6bGtjE8/tY8FBNhvylWTRseO7ou9LhQVHZk59Zdf7CWjYcNsUrjkEtvy8hbrbl/HgYwDxH0bR0AHz/8mUKsEISJNgYPGmEoRiQR6Al8ZY8pOcNhmoGqZLtSxrao84BfH82wUkXXYhLGstiegVH3TqJGdTqR/f7jzTrtt69ajE8Zrr8GLL9rHunQ5OmHEx9f/D83KSvj+e5sU/v1vKC62aytMngzjxtlLd95m67St5H+QT9cnuxJ8QbC7w6mV2rYgFgHnikgw8A32A/wqYOwJjlkGRIhIODYxjAaurrbPHGAMME1E2mAvOWXVPnzljfJn5JP1aBYlOSUEdAmg26RutBvrhZ8YVXToYEf4Xn65vV9aapdjPZQwfvrpyLrdgYHHtjI6dHBf7KciK+vIzKk5OdCypW0pXH+9vSznrWNL9q3Zx/rb19Py/JaEPR7m7nBqrVa9mERkpTGmr4hMABobY14QkWRjTPxJjrsEeAVbX3jPGDNJRCYCy40xc0VEgBeBoUAFMMkYM8tx7GJsSyUIKAD+bIyZf7zX0l5M3iF/Rj5rb15L5YHKw9t8mvgQNTXK65PEyWzefHQrY8UKm0jATg9SvZXh6kVtamv/fluonzYNfvzRJoE//MEmhREjvH/8SPm+clb2X0lZoWO8Q3vPurR0xgPlROQ34C/Ay9gP6lQRWW2M8ZiykSYI77A0bCklm0qO2R7QNYBB2YPcEJHnKik5upWxdKldzwDsh25i4tFJo337uovNGFiyxCaF2bNh3z7o0cMmhWuvbTi9t4wxZFybQf7H+cR9G0fw+Z53ackZ3VzvBh4GPnckh27AQmcFqNQhJTnHJocTbW/IAgLsKntnnQX33GO35eUdnTBefdWu9w12LqKqCSMuzvmtjLy8IzOnZmZCUJAd2Xz99TB4sPdeQjqebe9tI/+jfMKeDvPI5HAypzxQTkR8gCBjzB7XhHR6tAVR/x3MPsivEb9iyo/9nQwIDWBQrrYgTlVx8bGtjM2OriKNG9tCedWkcTrLahYX29lxp02Db7+1rYfzzrNJ4YorbJJoiPat3sfKASYm5h4AACAASURBVCtpPrg5cfPjPLZL6xm3IETkY+BWbJ1gGdBcRF41xvzdeWGqhmxv8l5WX7wa/EF8BVNSLUn4QNmuMvxbeciF9XoiMPDIh/8hublHF79feskORAPo1u3ohBEba6dEr76QkzHw1lvw4YeQkQG7d9veVo89ZmdO7d697s/Vk5TvKyd1ZCp+Lf2InhHtscnhZGpbg0g2xsSLyFigL/AQsMIYE+vqAGtLWxD1165vd5F6hf1jiv0qln3J+47qxRQyKoTNr26maUxT4r6Lw7+lJglnKi62Be+qrYytW+1jTZrYxNCxI3z5JUyZYqe+eO01yM62l6gOXUJKSvLsmVPrijGG9GvS2T5zO3HfxRGc5NmXlpxRg/AXEX/gT8BrxpgyEdGBaeqMbftoG2uvX0uTXk2I/SqWgE4BNO3d9JgeS8HnBbPmsjWsumgVcd/E4dfC3WM8vUdgoK0PDB5s7xtju6BWH8hXXm4nxQPbqrj3XnjiCWjRwm2he6St/9zK9hnbCZsY5vHJ4WRqm+/fBrKBptjRzl0Bj6pBqPrFGEPO8zlkXJNBi3NbkLA4gYBOx+/+13pYa3p/1pt9K/ex6uJVlO8tr8NoGxYR22129Ghb5P71V9izBxYvtiObAR5+2A7k0+RwtH2r9pE5IZPgC4Pp+khXd4dzxmqVIIwxU4wxnYwxlxhrE5B00gOVqoGpMGTemUnWQ1m0HdOW2K9ia9UiaDO8DdGfRLPn1z2svmQ15fs0SdSVxo1tneLXX+Hxx+18Ugu1H+NRyvc66g7BfvT6yPPnWaqNWiUIEWkhIi+JyHLHz4vY1oRSp6TioJ2sbPNrm+l8X2d6fdQLn4DaX7gOuTyE6JnRFC0tYvWlq6nYX+HCaNUhCxfaWsPs2TBxov131ChNEocYY1h3yzoOZh4kemY0jdrW87lQHGr7l/kesBcY5fjZA0xzVVDKO5XtKiPlwhR2ztlJj1d60P3v3RGfU/+W1XZkW3pN70XR4iJWD19NxQFNEq62bJlNCod6MSUl2fvLdNY0ALa+s5XtM7cTPjGclue1dHc4TnNKvZhOts2dtBeTZyveVMyqi1dxcMNBek3vRdtRp9HhvpptH20j49oMgn8fTJ+5ffANrIcrx6h6b1/KPlYMXEHL81oS+1XsaX3pcacT9WKqbQvioIicU+UJBwMHnRGc8n77UvaxctBKSraUEPdNnFOSA0D7ce2Jei+Kwu8KSb0slcqSypMfpJQTle+xdQf/1v70mt6r3iWHk6ltX8FbgQ9F5FCfhULgOteEpLxJ4YJC1ly2Br8WfiT8L4GgPs4dVtthfAdMuWHdTetYc8Ua+vy7Dz6NtDO+cj1jDGtvXsvBDQeJXxjvNXWHqmrbiynFGBMHxAKxxpgE4HyXRqbqvfyP81l18SoCuwaSsNT5yeGQjjd2JPKtSHZ9uYvUUalUlmlLQrnelre3sOOTHYQ/G07L33lP3aGqU/qqZYzZU2UOpntdEI/yAsYYcv6eQ/rYdFoMbkH84ngCQ107p3PHWzoS8VoEBf8pIG1MmiYJ5VJ7f9tL5t2ZBF8UTJcHvXe54zNpi3vXxTblFKbCkHl3JlkPZBEyKoTYr2PrbGqMTrd3oscrPdj5r52kj0unslyThHK+8j3lpI1Kw7+Nd9YdqjqT+Qp0qg11lIriCjKuyWDHZzsIvTf0tLuxnonQu0Ix5YYN921AfMX+AXvBgCXlGYwxrL1pLQc3HiT+h3gahXhf3aGqEyYIEdlLzYlAgMYuiUjVS2WFZawZsYaixUV0f7E7ne/tfPKDXKTzXztjyg1ZD2UhfkLPaT01SSin2PLWFnbM3kH438JpeY531h2qOmGCMMY0q6tAVP1VnOMY45B5kF4ze9FutPuXBu3yYBdMuWHjYxsRPyHq3SivvhSgXG/vSlt3aHVxK7o84L11h6p0Skx1RvatspPnVeyvIHZ+LMFDPGf2yq6PdsWUG7KfykZ8hci3IzVJqNNSXlRO6qhUGrVtRM8PezaY3yNNEOq0FS4sZM2f1uDbzJeExQkExXje0mFdn+hKZVklOZNyED8h4o0IpKGte6nOyKG6Q3F2MQk/JtCojXfXHarSBKFOS/6sfDKuzaBxZGNiv4olsLNru7GeLhEh/JlwTLkh9/lcxE/oMaWHJglVa1ve2MKOT3fQ7flutBjcsOY31wShTlnui7lsuG8DLX7Xgj5z+uAf7NkrvIkI3f7WDVNuyHsxD/ETur/UXZOEOqm9K/aSeW8mrS5pRef73Nfxwl1cOieBiAwVkbUikikiDx1nn1EikiYiqY61rw9tv05E1jt+dFoPD2AqDZn3ZLLhvg2EjAwhdn6sxyeHQ0SE7n/vTqe7OpH3Sh5ZD2RRm4kqVcNVte7Q60PvHu9wPC5rQYiIL/A6cCGQBywTkbnGmLQq+0QADwODjTGFItLWsb0V8CSQiO1mu8JxbKGr4lUnVlFcQcZ1GeyYvYNOd3Wix0s96t0fjIjQ4+Ue9nLTZHu5Kfz/wrUloY5hjCHjzxmU5JQQ/2M8/q3rxxchZ3PlJaYBQKYxJgtARGYBI4C0KvvcBLx+6IPfGLPdsf0i4FtjzC7Hsd8CQ4GZLoxXHUdZYRlr/rSGokVFdJ/cndB7Q+vth6qIEDElAlNuyHkuB/EXwieGuzss5WE2v7aZnf/aSbe/d6PF2Q2r7lCVKxNEJyC3yv08YGC1fSIBRGQJ4As8ZYz5+jjHdqr+AiJyM3AzQJcuDaNfcl0rznWMcVh3kF4f96LdGPePcThT4iNEvhGJKTdsemYT4ieEPRHm7rCUh9izfA8b/rqB1pe2duuAT0/g7iK1HxABDAFCgUUiElPbg40xU4GpYBcMckWADdm+1Y4xDnsriP06luDzPWeMw5kSHyFqahRUQPaT2YifeMUi8+rMlO0uI21UGo3aN6Ln+w1nvMPxuDJBbAaqpt9Qx7aq8oBfjDFlwEYRWYdNGJuxSaPqsT+4LFJ1jMIfHGMcmjrGOMR63hiHMyU+doS1KTdsfNSOuG4oI2TVsYwxrL1hLSW5JcQvarh1h6pc2YtpGRAhIuEi0ggYDcytts8cHIlARNpgLzllAfOBP4hIsIgEA39wbFN1YPsn21l10SoCOgbQd2lfr0wOh4ivEDUtiraj25L1YBa5L+ee/CDllTb/YzM7P99Jt+e60WJQw607VOWyFoQxplxE7sB+sPsC7xljUkVkIrDcGDOXI4kgDagA7jfGFACIyDPYJAMw8VDBWrlW7su5bLh3Ay3OdYxxaOX936J8/HzoOb0npsKw4d4NiJ8QOiHU3WGpOrTn1z1suG8Drf/YmtB79b0/RLylL3hiYqJZvny5u8Oot0ylYcP9G8h7KY82V7Sh10e98A30dXdYdaqyrJK0q9LY+flOIl6PoNNfjukXobxQWWEZK/quwBhD4srEBvGlqCoRWWGMSazpMV28V1FZUkna1WnkvZRHpwmd6P1J7waXHAB8/H2InhVN6+GtWX/7erZM3eLukJSLGWPIuD6DkrwSen/Su8Elh5PRBNHAle0uY9XQVez4ZAfdXuhGj1d7NOi1E3wa+dB7dm9aXdKKdbesY+t7W90dknKhvFfzKPhPAd1e6Ebzgc3dHY7H0QTRgBXnFZN8bjJFS4ro9VEvutzfpd4OgHMmnwAfev+rN8EXBbP2xrVs+2Cbu0NSLrDn1z1kPZBF6xGtCb1b6w410QTRQO1P3c9vg36jeFMxMfNiaDe2/g+AcybfQF/6fN6H4AuCybg+g/wZ+e4OSTlR2a4yO89Sx0Z2xUH9YlQjTRAN0O5Fu/ntnN8wFYb4RfG0+n0rd4fkkXwb+9LnP31oOaQl6dems/2T7Sc/SHm8Q3WH0i2l9J7du95MOOkOmiAamO2fbiflwhQatW9E36V9aRavq8qeiG8TX2K+iKHFOS1IG5vG9s80SdR3eS/nUTC3gO5/707zAVp3OBFNEA1I3qt5pF2VRrP+zUhYkkBgV89c5MfT+Db1Jea/MTQ/qznpY9LZMWeHu0NSp6no5yKyHsyizWVt6HSndmM+GU0QDcChMQ6Zd2fS5k9tiPs2TrvznSK/Zn7EzoulWWIz0kalsfOLne4OSZ2isl1lpF2VRkBoAFHvRWndoRY0QXi5ypJK0selkzs5l463d6T3p73xbdzwxjg4g19zP2K/jiUoPojUK1MpmFfg7pBULRljyBifQenWUqJnR+PfUr8g1YYmCC9WXlTOqktWsX3mdro9142If0Q06DEOzuDXwo/Yb2JpGtOUNZevYdd8nQGmPsh7KY+CLwroPrk7zftr3aG2NEF4qZLNJfz2u98oWlREzw970uVBHePgLP4t/Yn7Jo6mvZqy5k9rKFygCx16sqKlRWQ9lEWby9vQaYLWHU6FJggvtD9tPysHraQ4y45xaH9Ne3eH5HX8W/kT+20sjSMas/qPqyn8QZOEJyorcNQdOgcQ9U+tO5wqTRBeZvfi3fw2+DdMmWOMw4U6xsFVGrVpRNyCOAK7BbJ62Gp2L97t7pBUFabSkH5dOqX5pfT+tLfWHU6DJggvsuNfO0i5MAX/dv4kLE2gWYKOcXC1RiGNiF8QT2CXQFZdvIqiJUXuDkk55L6Yy64vd9H9xe4066d/C6dDE4SXyPtHHqkjU2nWtxl9l/SlcVhjd4fUYDRq14i47+MI6BRgk8TPmiTcreinIrIeziLkyhA63a51h9OlCaKeM5WGDQ9uIPPOTNqMaEPcgjhdKtENAjoEEP99PP5t/Vl10Sr2LNvj7pAarNKdpaRdlUZg10Ci3tW6w5nQBFGPVZZWkn5tOrkv5NLxto70/kzHOLhTQKcA4hfatYxX/WEVe1fudXdIDY6pNGRcl0Hpdlt38GvhskUzGwRNEPVU+R7HGIcZ2wmfFE7E6zrGwRMEdg4kfmE8vi18Sfl9CnuTNUnUpdy/57Jr3i56vNyDZn217nCmNEHUQyVbHGMcfiyi5/s96fpIV21Ge5DAro4kEWSTxL7V+9wdUoOw+3+7yXo0i5CRIXS8raO7w/EKmiDqmf3pdozDwcyDxPw3hvbX6RgHT9Q4vDFx38fhE+hDygUp7E/b7+6QvFrpzlLSRqcRGKZ1B2fSBFGPFC0p4rfBv1FZUknCjwm0ukjHOHiyJj2aEP99POInJJ+fzP4MTRKuYCoNGddkULajzNYdmmvdwVk0QdQTOz7fQcrvU/AP8bfrOGi/7nqhSWQT4r6PAyDl/BQOrDvg5oi8T84LOez6ehc9XumhY3+czKUJQkSGishaEckUkYdqeHy8iOwQkWTHz41VHnteRNY4fq5yZZyebvPrm0m9IpWg+CASliTQOFzHONQnTXs2Jf77eEy5ITkpmQOZmiScZffi3Wx8bCMhV4XQ8VatOzibyxKEiPgCrwMXA9HAGBGJrmHXT4wx8Y6fdx3HDgP6AvHAQOA+EWlwUzAaY8h6OIv1d6yn9R9bE7cgjkZtGrk7LHUamkY3Je77OCpLKkk5P4WDGw+6O6R6r3SHrTs07taYqKlad3AFV7YgBgCZxpgsY0wpMAsYUctjo4FFxphyY8x+YBUw1EVxeqTK0koyrssg57kcOtzSgd7/6o1vEx3jUJ8F9QkifkE8FfsrSE5KpnhTsbtDqrdMpSH9mnTKCsqInh2tdQcXcWWC6ATkVrmf59hW3RUiskpEPhORzo5tKcBQEWkiIm2AJKBz9QNF5GYRWS4iy3fs8J5lIMv3lrP60tXkT88n/NlwIt+MxMdPy0XeICguiLhv46gociSJXE0SpyPnuRwK5xcS8WqErqvuQu7+1PkCCDPGxALfAh8AGGO+AeYBPwEzgaVARfWDjTFTjTGJxpjEkJCQuovahUq2lpB8XjKF3xcSNS2Kro/qGAdv06xvM2K/jaVsVxnJScmUbC5xd0j1yu5Fu9n4+EbajmlLh5s7uDscr+bKBLGZo7/1hzq2HWaMKTDGHPrreBfoV+WxSY66xIWAAOtcGKtH2J9hxzgcWHeAmC9i6DBef/m9VfPE5sTNj6NsuyNJbNUkURul2x11h+6NiXw7Ur88uZgrE8QyIEJEwkWkETAamFt1BxGp+gk4HEh3bPcVkdaO27FALPCNC2N1u6KfHGMcDlYS/0M8rS9u7e6QlIs1H9ic2K9jKd1aSsr5KZTml7o7JI9mKg3p49IpLyy34x2aad3B1VyWIIwx5cAdwHzsB/9sY0yqiEwUkeGO3e4UkVQRSQHuBMY7tvsDi0UkDZgKjHM8n1faMWcHKRek4N/KjnFontjgOmw1WC3ObkHMvBiKc4pJPj+Z0u2aJI5n0/9tovDbQnpM6UFQXJC7w2kQxBjj7hicIjEx0SxfvtzdYZyyzW9uZv0d62mW2IyY/8bQKES7sTZEhT8UsvqS1TTuYafo0O7MRyv8oZCUC1JoO7otvT7qpZeWnEhEVhhjEmt6zN1F6gbLGEPWo1ms/8t6Wl/Smvjv4zU5NGDBQ4KJ+SKGg+sPkvL7FMp2lbk7JI9Rml9K+ph0Gkdo3aGuaYJwg8qySjKuzyDn/3LocFMHen/eG9+mOsahoQu+IJg+/+nDgYwDpFyYQlmhJglT4ag77C6n9+ze+AVp3aEuaYKoY+V7y1n9x9Xkf5BP2NNhRL6tYxzUEa3+0Io+/+7D/jX7WXXRKsqLvLb0Viub/m8Thd8V0uMfPQiK1bpDXdNPpjpUsq2E5CHJFH5XSNS7UYQ9EabNZXWM1pe0pvdnvdmXvI9VQ1dRvqdhJonChYVkP5VNu3Ht6PBn7fLtDpog6siBdQf47ezfOJBxgJi5MfoLr06ozR/bED07mr3L97Lq4lWU721YSaJkWwlpY9JoEtmEiDcj9IuUm2iCqANFPxex8uyVVOyrsGMcLtExDurkQv4UQvSsaPb8sofVw1ZTsf+YyQS8kqkwpI9Np2JPBdGfRmvdwY00QbjYzrk7STk/Bb+WfiT8lEDz/jrGQdVeyBUhRM+IpmhJEav/uJqKA96fJDY9u4nd3+8m4rUIgvpo3cGdNEG40Ja3t7DmsjU07dOUvj/1pUmPJu4OSdVDba9qS6/pvdj9427WjFhDxUHvTRKF3xeS/XQ27a5tR/vrdTldd9ME4QLGGDY+sZF1t66j1dBWxC+Mp1FbHeOgTl+7q9vRc1pPChcUsuayNVQUe1+SKNlWQtrVaTTp2YTIN3S8gyfQBOFklWWVrP3zWjY9s4n2f25Pn//00TEOyinaX9ueqHejKJxfSOoVqVSWVLo7JKcxFYb0qx11h9nR+jfjITRBOFH5vnLWDF/Dtmnb6PpkV6LeidIxDsqpOtzQgci3I9k1bxepI1OpLPWOJJE9MZvdC3cT8YbWHTyJdg9wktL8UlYNW8W+5H1EvhNJxxt1fVzlGh1v7oipMKz/y3rSRqcR/Uk0Pv7194vIru92semZTbS7rp1Oce9h6u9vlQc5sP4AK89eyYG0A/SZ00eTg3K5Trd1oseUHuz8fCfpV6dTWV4/WxIlW0tIH5tOk15NiHw90t3hqGq0BXGG9vxq+6gDxC+Mp/lA7caq6kbohFBMuWHDvRsQP6Hn9J716pJmZXklaWPS7PighfFad/BAmiDOwM7/7iTtqjQatW9E7NexNInQbqyqbnW+pzOm3JD1QBb4Qq8PeiG+9aP3z6aJmyj6sYie7/ekaXRTd4ejaqAJ4jRteWcL625dR7O+jnUc2mk3VuUeXe7vgik3bHxko21JvNcT8fHsJLHrm11senYT7a9vT/vrdLyDp9IEcYqMMWQ/lc2miZtodXEromfrVADK/bo+3BVTbsh+IhvxE6KmRnlskijZUkL6uHSaRDch4rUId4ejTkA/2U5BZXkl625dx7Z/bqP99e3tVN31uPeI8i5hj4dhyg2bJm5CfIXINyM9LkkcrjvsryD+03h8m2jdwZNpgqiliv0VpI5KZde8XXR9vCthT+tU3crzhD0Vhikz5PwtB/ETIl7zrJlQs5/KpmhRET0/7EnTXlp38HSaIGqhdHspqy9dzd4Ve4l8K5KOt2g3VuWZRITwSeGYckPu33MRf6HHyz08Iknsmr+LnP/Lof2f29P+Gq071AeaIE7iQOYBVg1dRemWUvp83oc2w9u4OySlTkhE6PZ8N0y5Ie/lPMRX6D65u1uTRMlmW3do2rspEVO07lBfaII4gT3L7BgHU2mI+z6OFme1cHdIStWKiND9xe42SbyUh/gJ3Z7r5pYkcbjucNCu76B1h/rDpRVWERkqImtFJFNEHqrh8fEiskNEkh0/N1Z57AURSRWRdBGZInX8m13wZQHJQ5LxDfKl7099NTmoekdE6PFqDzre1pHcF3LZ+PhGjDF1Hkf2E9kULS4i6u0omvbUukN94rIWhIj4Aq8DFwJ5wDIRmWuMSau26yfGmDuqHXs2MBiIdWz6H3Ae8IOr4q1q6z+3svaWtQTFBRHzZQwB7QPq4mWVcjoRW6g25YacSTn4+PsQ9mRYnb1+wdcF5Pwthw43dqDd2HZ19rrKOVx5iWkAkGmMyQIQkVnACKB6gqiJAQKBRoAA/kC+i+I88qLGsOmZTWQ/mU3wRcH0/rQ3fs30Kpyq38RHiHwr0o6TeCobfCHssTCXv25xXrGtO8Q0pceUHi5/PeV8rvz06wTkVrmfBwysYb8rROR3wDrgHmNMrjFmqYgsBLZiE8Rrxpj06geKyM3AzQBdunQ5rSDzZ+ST9WgWJTkl+DT1oXJfJe2ua2en6tYxDspLiI8Q9U4UpsKQ/bgdTNf1oa4ue73K8krSRqdhSgy9P+2Nb2OtO9RH7v4E/AIIM8bEAt8CHwCISA+gFxCKTTTni8i51Q82xkw1xiQaYxJDQkJO+cXzZ+Sz9ua1lGwqAQOV+yoRPyH4wmBNDsrriK+dhqPt1W3Z+PBGcibnuOy1sh/PZs+SPUROjaRJlM5RVl+58lNwM9C5yv1Qx7bDjDEFxpgSx913gX6O25cBPxtj9hlj9gFfAYOcHWDWo1lUHjh6mmRTbtj46EZnv5RSHkF8hZ4f9CTkqhCy7s8i95Xckx90igrmFZDzXA4dbu5AuzFad6jPXJkglgERIhIuIo2A0cDcqjuISNXVQYYDhy4j5QDniYifiPhjC9THXGI6UyU5Jae0XSlv4OPnQ6/pvWhzRRs23LOBza9vPvlBtVScW0z6tek0jWtKj1e07lDfuSxBGGPKgTuA+dgP99nGmFQRmSgiwx273enoypoC3AmMd2z/DNgArAZSgBRjzBfOjjGgS829k463XSlv4ePvQ/TMaNr8qQ3r71jP5rfOPElUllWpO8zWuoM3EHf0i3aFxMREs3z58lM65lANouplJp8mPkRNjdIueapBqCytJPXKVAq+KDjjpXI3PLiB3Bdy6TWzF+1G699PfSEiK4wxiTU91qArse3GtiNqahQBXQNAIKBrgCYH1aD4NPKh96e9aXVxK9bdvI6t7289recp+LKA3Bdy6XhrR00OXqTBd/JvN7adJgTVoPkE+ND7371ZM3wNa29Yi/gJ7cfVfjK94pwjdYfuL3d3YaSqrjXoFoRSyvIN9KXPf/rQMqklGddlkD+zduNSD9cdyhzjHQK17uBNNEEopQDwbexLzBcxtPxdS9LHpbN99vaTHrPxkY3sWbqHqHeidE12L6QJQil1mG8TX/p80YcWg1uQdnUaO/6947j77vxiJ7mTc+l4W0faXtW2DqNUdUUThFLqKH5BfsR8GUPzgc1JuyqNnf/Zecw+xZuKybgug6CEILq/pHUHb6UJQil1DL9mfsR+FUtQvyBSR6ay879HkkRlaSWpV6Viyg3Rs6O17uDFGnwvJqVUzfya+xH7dSyrLlxF6hWpdLqrEztm77BzlwEdJ3SkSQ+tO3gzbUEopY7Lv6U/sd/E0qhDI/L+nnc4OQBs++c28me4fBZ+5UaaIJRSJ+Qf7A8Vx26vPFBJ1qNZdR+QqjOaIJRSJ1WyWSe2bIg0QSilTkontmyYNEEopU6q26Ru+DQ5+uPCp4kP3SZ1c1NEqi5oglBKnZRObNkwaTdXpVSt6MSWDY+2IJRSStVIE4RSSqkaaYJQSilVI00QSimlaqQJQimlVI3EGOPuGJxCRHYAm87gKdoAx85rXP94y3mAnoun8pZz8ZbzgDM7l67GmJCaHvCaBHGmRGS5MSbR3XGcKW85D9Bz8VTeci7ech7gunPRS0xKKaVqpAlCKaVUjTRBHDHV3QE4ibecB+i5eCpvORdvOQ9w0bloDUIppVSNtAWhlFKqRpoglFJK1ahBJQgReU9EtovImuM8LiIyRUQyRWSViPSt6xhrqxbnMkREikQk2fHzRF3HWBsi0llEFopImoikishdNexTL96XWp6Lx78vIhIoIr+KSIrjPJ6uYZ8AEfnE8Z78IiJhdR/pydXyXMaLyI4q78mN7oi1tkTEV0R+E5H/1vCYc98XY0yD+QF+B/QF1hzn8UuArwABzgJ+cXfMZ3AuQ4D/ujvOWpxHB6Cv43YzYB0QXR/fl1qei8e/L47/5yDHbX/gF+Csavv8BXjLcXs08Im74z6DcxkPvObuWE/hnO4FPq7p98jZ70uDakEYYxYBu06wywjgQ2P9DLQUkQ51E92pqcW51AvGmK3GmJWO23uBdKBTtd3qxftSy3PxeI7/532Ou/6On+q9WUYAHzhufwZcICJSRyHWWi3Ppd4QkVBgGPDucXZx6vvSoBJELXQCcqvcz6Me/oFXMcjRtP5KRHq7O5iTcTSHE7Df8qqqd+/LCc4F6sH74riMkQxsB741xhz3PTHGlANFQOu6jbJ2anEuAFc4Ll9+JiKd6zjEU/EK8ABQeZzHnfq+aILwXiuxc6zEAf8A5rg5nhMSkSDgX8Ddxpg97o7nTJzkXOrF+2KMqTDGxAOhwAAR6ePumE5XLc7lCyDMGBMLfMuRb+AeRUQuBbYbY1bU1WtqgjjaZqDqt4dQx7Z6us2lgwAAA2tJREFUxxiz51DT2hgzD/AXkTZuDqtGIuKP/UCdYYz5dw271Jv35WTnUp/eFwBjzG5gITC02kOH3xMR8QNaAAV1G92pOd65GGMKjDEljrvvAv3qOrZaGgwMF5FsYBZwvoh8VG0fp74vmiCONhe41tFr5iygyBiz1d1BnQ4RaX/o2qOIDMC+1x73B+yI8Z9AujHmpePsVi/el9qcS314X0QkRERaOm43Bi4EMqrtNhe4znH7SuB746iMepLanEu1etZwbO3I4xhjHjbGhBpjwrAF6O+NMeOq7ebU98XvdA+sj0RkJrYXSRsRyQOexBatMMa8BczD9pjJBA4A17sn0pOrxblcCdwmIuXAQWC0J/4BY78VXQOsdlwnBngE6AL17n2pzbnUh/elA/CBiPhiE9hsY8x/RWQisNwYMxebCKeLSCa2s8Ro94V7QrU5lztFZDhQjj2X8W6L9jS48n3RqTaUUkrVSC8xKaWUqpEmCKWUUjXSBKGUUqpGmiCUUkrVSBOEUkqpGmmCUOokRKSiykyfySLykBOfO0yOMyOvUu7WoMZBKHWaDjqmalCqQdEWhFKnSUSyReQFEVntWHOgh2N7mIh875j8bYGIdHFsbycinzsm6ksRkbMdT+UrIu841iv4xjHiFxG5U+zaEqtEZJabTlM1YJoglDq5xtUuMV1V5bEiY0wM8Bp2pk2wk/B94Jj8bQYwxbF9CvCjY6K+vkCqY3sE8LoxpjewG7jCsf0hIMHxPLe66uSUOh4dSa3USYjIPmNMUA3bs4HzjTFZjkn6thljWovITqCDMabMsX2rMaaNiOwAQqtMDHdoWvBvjTERjvsPAv7GmGdF5GtgH3bG1zlV1jVQqk5oC0KpM2OOc/tUlFS5XcGR2uAw4HVsa2OZY3ZOpeqMJgilzsxVVf5d6rj9E0cmSRsLLHbcXgDcBocXsWlxvCcVER+gszFmIfAgdtrmY1oxSrmSfiNR6uQaV5mdFeBrY8yhrq7BIrIK2woY49g2AZgmIvcDO/6/vTu2QRgIggC4J7fkjoiI3ItDxy6PHp6Al5wcCRKQzFTw2Wr/pLtc22e3JEdV3fJqCvck79aWL0nOGSKVZJ/3DOBnzCDgQ3MGsY4xHv9+C3yDLyYAWhoEAC0NAoCWgACgJSAAaAkIAFoCAoDWE8SfCnPiYbxWAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_generator = datagen.flow_from_directory(\n",
        "test_directory,\n",
        "target_size=(150, 150),\n",
        "batch_size = 25,\n",
        "class_mode='binary')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DH_VkSA337g8",
        "outputId": "06f9851f-2c42-4d19-8f0e-63475f27cecc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 353 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_loss, test_accuracy = new_model.evaluate(test_generator, steps=4)\n",
        "print('test accuracy: ' + str(test_accuracy*100) + '%')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HddMWGTb3-m5",
        "outputId": "baa95081-6129-418a-d323-c4f92bb9ae7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4/4 [==============================] - 25s 6s/step - loss: 0.6347 - acc: 0.7300\n",
            "test accuracy: 73.00000190734863%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "if os.getcwd() != '/content':\n",
        "  os.chdir('/content')"
      ],
      "metadata": {
        "id": "tqPW5Q5m4Ayt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from google.colab import files\n",
        "from keras.preprocessing import image\n",
        "\n",
        "uploaded = files.upload()\n",
        "\n",
        "for fn in uploaded.keys():\n",
        "  path = '/content/' + fn\n",
        "  img = image.load_img(path, target_size=(150, 150))\n",
        "  x = image.img_to_array(img)\n",
        "  x = np.expand_dims(x, axis=0)\n",
        "  images = np.vstack([x])\n",
        "  probability = new_model.predict(images, batch_size=10)\n",
        "  if probability > 0.5:\n",
        "    print('Image is of a unCoated tongue.')\n",
        "  elif probability < 0.5:\n",
        "    print('Image is of an coated tongue.')\n",
        "  else:\n",
        "    print('Image is ambiguous. ')\n",
        "  os.remove(path)\n",
        "img_array=tf.keras.utils.img_to_array(img)\n",
        "img_array=tf.expand_dims(img_array,0)\n",
        "predictions=model.predict(img_array)\n",
        "score=tf.nn.softmax(predictions[0])\n",
        "print(\n",
        "    \"This image most likely belongs to {} with a {:.2f} percent confidence.\"\n",
        "    .format(class_names[np.argmax(score)], 100 * np.max(score))\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 107
        },
        "id": "YS8nXn6C4D02",
        "outputId": "c6d9a9ca-94bb-48b8-ac72-c6ab41e70a55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-9e7504d5-51a2-450e-b264-3e432936a6c3\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-9e7504d5-51a2-450e-b264-3e432936a6c3\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving 20211228_115758 - Arunava Banerjee.jpg to 20211228_115758 - Arunava Banerjee.jpg\n",
            "Image is of an coated tongue.\n",
            "This image most likely belongs to Coated tongue with a 100.00 percent confidence.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_model.save(\"model/tongue.h5\")"
      ],
      "metadata": {
        "id": "dgIFgwMVNfxm"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}